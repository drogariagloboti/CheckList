# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\\\Users\\\\marcelo.melo\\\\Downloads\\\\PycharmProjects\\\\CheckList\\\\app.py'],
    pathex=['C:\\Users\\marcelo.melo\\Downloads\\PycharmProjects\\CheckList\\venv2\\Lib\\Lib\\site-packages'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='win7app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\marcelo.melo\\Downloads\\PycharmProjects\\CheckList\\logo_globo.ico'],
)
