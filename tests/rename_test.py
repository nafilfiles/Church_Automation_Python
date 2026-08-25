import pathvalidate as pv
import platform


def test_validation():
    os = platform.system()
    if os == "Windows":
        # Should return true as valid filenames
        assert pv.is_valid_filename("validname.txt", platform="auto")
        assert pv.is_valid_filename("123456790", platform="auto")
        assert pv.is_valid_filename("qwertyuiopasdfghjklzxcvbnm", platform="auto")
        assert pv.is_valid_filename("!@#$%^&()", platform="auto")
        assert pv.is_valid_filename(r"-_=+[{}]'';.,~`", platform="auto")

        # Should return false as invalid filenames
        assert not pv.is_valid_filename("invalid<name>.txt", platform="auto")
        assert not pv.is_valid_filename("invalid:name", platform="auto")
        assert not pv.is_valid_filename('invalid"name".txt', platform="auto")
        assert not pv.is_valid_filename("invalid/name", platform="auto")
        assert not pv.is_valid_filename(r"invalid\ name.txt", platform="auto")
        assert not pv.is_valid_filename("invalid|name.txt", platform="auto")
        assert not pv.is_valid_filename("invalid?name.txt", platform="auto")
        assert not pv.is_valid_filename("invalid*name.txt", platform="auto")

    if os == "Linux":
        assert pv.is_valid_filename("validname.txt", platform="auto")
        assert pv.is_valid_filename("123456790", platform="auto")
        assert pv.is_valid_filename("qwertyuiopasdfghjklzxcvbnm", platform="auto")
        assert pv.is_valid_filename("!@#$%^&*()", platform="auto")
        assert pv.is_valid_filename(r"-_=+{}[]\|'';:.>,<?`~", platform="auto")
        assert not pv.is_valid_filename("invalid/name.txt", platform="auto")

    if os == "Darwin": # MacOs
        assert pv.is_valid_filename("validname.txt", platform="auto")
        assert pv.is_valid_filename("123456790", platform="auto")
        assert pv.is_valid_filename("qwertyuiopasdfghjklzxcvbnm", platform="auto")
        assert pv.is_valid_filename("!@#$%^&*()", platform="auto")
        assert pv.is_valid_filename(r"-_=+{}[]\|'';/.>,<?`~", platform="auto")
        assert not pv.is_valid_filename("invalid:name.txt", platform="auto")

    
