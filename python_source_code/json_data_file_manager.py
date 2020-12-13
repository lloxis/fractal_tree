import json

class manager:
    """
    read and write a json file
    """
    def __init__(self, path, default_datas):
        self.datas = None
        self.path = path
        self.default_datas = default_datas

        self.read_file()

    def read_file(self):
        """
        Read the file and save the converted data to self.datas
        Also check and andle read errors
        """
        try:
            print("laoding", self.path)
            file_read = open(self.path, "r")
            self.datas = json.load(file_read)
            file_read.close()

            # check and reset if keys are mising ; WILL NORMALY NEVER APPEND
            for key in self.default_datas.keys():
                if key not in self.datas:
                    print("XXX key \"" + key + "\" not found. key will be created")
                    self.datas[key] = self.default_datas[key]
                    self.write_datas(reason="key missing")

            print(self.path, "file loaded")
            print("datas : ")
            print(self.datas)

        # if we were not able to find the file
        except FileNotFoundError:
            print("XXX", self.path, "not found. File will be created")
            # we create the file with it's default datas
            self.datas = self.default_datas
            self.write_datas(reason="file not found")

        # if there is an error while trying to read the file
        except json.decoder.JSONDecodeError:
            print("XXX", self.path, "error while trying to read file. File will be reset to default")
            self.datas = self.default_datas
            self.write_datas(reason="reseting file")

    def write_datas(self, reason="None"):
        """
        write the value of self.datas to the json file
        """
        file_write = open(self.path, "w")
        json.dump(self.datas, file_write, indent=4)
        file_write.close()
        print(self.path, "file created or updated, reason : " + reason)
        print("datas : ")
        print(self.datas)