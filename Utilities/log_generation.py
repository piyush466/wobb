import logging

class LogGen:

    @staticmethod
    def logger():
        logg = logging.getLogger(__name__)
        filehandle = logging.FileHandler(r"C:\Users\Cliffex-Lead\wobb\Logs\log1.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        filehandle.setFormatter(formatter)
        logg.addHandler(filehandle)
        logg.setLevel(logging.INFO)
        logg.setLevel(logging.DEBUG)
        return logg
