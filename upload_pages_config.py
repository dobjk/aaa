from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parent
def git(*args):
 subprocess.run(['git',*args],cwd=ROOT,check=True)
try:
 if not (ROOT/'.git').exists():raise RuntimeError('请先将这些文件放入已有的 aaa 本地仓库目录，不要建立新仓库。')
 branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
 if branch!='main':raise RuntimeError('请先切换至 main 分支')
 print('当前远程仓库：',flush=True);git('remote','-v')
 staged=subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT)
 if staged.returncode:raise RuntimeError('已有暂存修改，请先提交或取消暂存')
 git('add','--','.github/workflows/pages.yml','build_pages.py','upload_pages_config.py','PAGES_SETUP.md')
 if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
  git('commit','-m','Configure article website and GitHub Pages deployment')
 git('push','origin','main')
 print('配置上传完成。在 GitHub 仓库 Settings → Pages → Source 选择 GitHub Actions。')
except Exception as exc:
 print('失败：',exc);sys.exit(1)
