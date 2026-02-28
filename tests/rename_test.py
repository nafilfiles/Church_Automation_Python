import pathvalidate as pv
import platform


def test_validation():
    os = platform.system()
    if os == "Windows":
        # Should return true as valid filenames
        assert pv.is_valid_filename("validname.txt")
        assert pv.is_valid_filename("123456790")
        assert pv.is_valid_filename("qwertyuiopasdfghjklzxcvbnm")
        assert pv.is_valid_filename("!@#$%^&()")
        assert pv.is_valid_filename(r"-_=+[{}]'';.,~`")

        # Should return false as invalid filenames
        assert not pv.is_valid_filename("invalid<name>.txt")
        assert not pv.is_valid_filename("invalid:name")
        assert not pv.is_valid_filename('invalid"name".txt')
        assert not pv.is_valid_filename("invalid/name")
        assert not pv.is_valid_filename(r"invalid\ name.txt")
        assert not pv.is_valid_filename("invalid|name.txt")
        assert not pv.is_valid_filename("invalid?name.txt")
        assert not pv.is_valid_filename("invalid*name.txt")

    if os == "Linux":
        assert pv.is_valid_filename("validname.txt")
        assert pv.is_valid_filename("123456790")
        assert pv.is_valid_filename("qwertyuiopasdfghjklzxcvbnm")
        assert pv.is_valid_filename("!@#$%^&*()")
        assert pv.is_valid_filename(r"-_=+{}[]\|'';:.>,<?`~")
        assert not pv.is_valid_filename("invalid/name.txt")

    if os == "Darwin": # MacOs
        assert pv.is_valid_filename("validname.txt")
        assert pv.is_valid_filename("123456790")
        assert pv.is_valid_filename("qwertyuiopasdfghjklzxcvbnm")
        assert pv.is_valid_filename("!@#$%^&*()")
        assert pv.is_valid_filename(r"-_=+{}[]\|'';/.>,<?`~")
        assert not pv.is_valid_filename("invalid:name.txt")

    
