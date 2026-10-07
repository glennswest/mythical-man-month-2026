import os,re,subprocess,json,sys
EXT={".rs":"Rust",".sh":"Shell",".bash":"Shell",".py":"Python",".go":"Go",".c":"C",".h":"C",".cc":"C++",".cpp":"C++",".js":"JavaScript",".mjs":"JavaScript",".cjs":"JavaScript",".ts":"TypeScript",".svelte":"Svelte",".swift":"Swift",".html":"HTML",".css":"CSS",".nix":"Nix",".lua":"Lua",".pl":"Perl",".rb":"Ruby",".java":"Java",".kt":"Kotlin",".zig":"Zig",".S":"Assembly",".s":"Assembly",".asm":"Assembly",".bpf.c":"C"}
SKIPDIR=re.compile(r'(^|/)(tests?|testdata|test-data|fixtures?|benches?|examples?|e2e|vendor|third_party|3rdparty|docs?|node_modules|target|dist|build|golden|goldens|testing|spec|specs|mocks?|scripts|deploy|tools|hack|packaging|ci|\.github|bench|xtask|model|conformance|pxeimage|proto)(/|$)', re.I)
SKIPFILE=re.compile(r'(^build\.rs$|^Makefile$|^ci-[^/]*\.sh$|^build[^/]*\.sh$|^rebuild\.sh$|^install-[^/]*\.sh$|^vendor\.sh$|^strip_annotations\.py$|^import-[^/]*\.py$|_test\.(go|py|rs)$|^test_.*\.py$|\.test\.(js|ts|mjs)$|\.spec\.(js|ts)$|(^|/)check-[^/]*\.sh$|(^|/)test[^/]*\.sh$)', re.I)
def strip_rust_tests(src):
    out=[];i=0;n=len(src)
    while True:
        m=re.search(r'#\[cfg\(test\)\]\s*(pub\s+)?mod\s+\w+\s*\{',src[i:])
        if not m: out.append(src[i:]);break
        s=i+m.start(); out.append(src[i:s]); j=i+m.end(); depth=1
        while j<n and depth:
            c=src[j]
            if c=='"':
                j+=1
                while j<n and src[j]!='"': j+= 2 if src[j]=='\\' else 1
            elif c=='/' and src[j:j+2]=='//':
                j=src.find('\n',j); j=n if j<0 else j
            elif c=='{': depth+=1
            elif c=='}': depth-=1
            j+=1
        i=j
    return ''.join(out)
def code_lines(text,lang):
    lines=0;block=False
    cmt={"Rust":"//","C":"//","C++":"//","Go":"//","JavaScript":"//","TypeScript":"//","Swift":"//","Kotlin":"//","Java":"//","Zig":"//","Svelte":"//","CSS":None,"HTML":None}.get(lang)
    hashc=lang in ("Shell","Python","Perl","Ruby","Nix")
    for l in text.splitlines():
        t=l.strip()
        if not t: continue
        if block:
            if '*/' in t: block=False
            continue
        if cmt and t.startswith('/*'):
            if '*/' not in t: block=True
            continue
        if cmt and t.startswith(cmt): continue
        if hashc and t.startswith('#') and not t.startswith('#!'): continue
        lines+=1
    return lines
res={}
for r in sorted(os.listdir('.')):
    if not os.path.isdir(os.path.join(r,'.git')): continue
    files=subprocess.run(['git','-C',r,'ls-files'],capture_output=True,text=True).stdout.split('\n')
    langs={}
    for f in files:
        if not f or SKIPDIR.search(f) or SKIPFILE.search(os.path.basename(f)) or SKIPFILE.search(f): continue
        ext='.bpf.c' if f.endswith('.bpf.c') else os.path.splitext(f)[1]
        lang=EXT.get(ext)
        if not lang: continue
        try: t=open(os.path.join(r,f),encoding='utf-8',errors='ignore').read()
        except Exception: continue
        if lang=="Rust": t=strip_rust_tests(t)
        langs[lang]=langs.get(lang,0)+code_lines(t,lang)
    res[r]=langs
json.dump(res,open('../loc.json','w'),indent=0)
tot=sum(sum(v.values()) for v in res.values()); rust=sum(v.get("Rust",0) for v in res.values())
print("shipped code lines %d, Rust %d (%.1f%%)"%(tot,rust,100*rust/tot))
