from alphalauncher import main


def test_pex_launcher():
    assert main.launch_pex() == "2.1.56"
