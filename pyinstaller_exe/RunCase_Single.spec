# -*- mode: python -*-

block_cipher = None


a = Analysis(['G:\\Web_MaiTianOnLineAutoTest\\test\\RunCase\\RunCase_Single.py'],
             pathex=['G:\\Web_MaiTianOnLineAutoTest\\test\\denglu_TestCase\\login_testcase.py', '', 'G:\\Web_MaiTianOnLineAutoTest\\pyinstaller_exe'],
             binaries=[],
             datas=[],
             hiddenimports=['test.common_package.weituo', 'test.common_package.myunit', 'test.common_package.bj_fz_xm_for_bianli', 'test.denglu_TestCase.loginPage', 'test.common_package.shouye_search', 'test.common_package.pgbo_check', 'test.common_package.selectcity'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='RunCase_Single',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='RunCase_Single')
