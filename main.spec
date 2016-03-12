# -*- mode: python -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['/Users/LittleBreadLoaf/Documents/Interspellar_server'],
             binaries=None,
             hiddenimports=[],
	datas=[
	( '/Users/LittleBreadLoaf/Documents/Interspellar_server/resources', 'resources')
		],
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
          name='main',
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
               name='main')
