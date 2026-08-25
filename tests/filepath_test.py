import platform
import pathvalidate as pv

def test_validation():
    os = platform.system()
    if os == "Windows":

        # Should return true as valid filepaths
        assert pv.is_valid_filepath("C:/validname.txt", platform=os)
        # assert pv.is_valid_filepath("/validname.txt", platform=os)
        assert pv.is_valid_filepath("C:/Users/Me/Documents/validname.txt", platform=os)
        assert pv.is_valid_filepath("C:/User123/validname.txt", platform=os)

        # Should return false as invalid filenames
    #     assert not rename.validation("invalid<name>.txt")
    #     assert not rename.validation("invalid:name")
    #     assert not rename.validation('invalid"name".txt')
    #     assert not rename.validation("invalid/name")
    #     assert not rename.validation(r"invalid\ name.txt")
    #     assert not rename.validation("invalid|name.txt")
    #     assert not rename.validation("invalid?name.txt")
    #     assert not rename.validation("invalid*name.txt")

    # if os == "Linux":
    #     assert rename.validation("validname.txt")
    #     assert rename.validation("123456790")
    #     assert rename.validation("qwertyuiopasdfghjklzxcvbnm")
    #     assert rename.validation("!@#$%^&*()")
    #     assert rename.validation(r"-_=+{}[]\|'';:.>,<?`~")
    #     assert not rename.validation("invalid/name.txt")

    # if os == "Darwin": # MacOs
    #     assert rename.validation("validname.txt")
    #     assert rename.validation("123456790")
    #     assert rename.validation("qwertyuiopasdfghjklzxcvbnm")
    #     assert rename.validation("!@#$%^&*()")
    #     assert rename.validation(r"-_=+{}[]\|'';/.>,<?`~")
    #     assert not rename.validation("invalid:name.txt")

    
