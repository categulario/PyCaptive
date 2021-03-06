#!/usr/bin/python3

""" PyCaptive: Standalone Mode """

if __name__ == "__main__":
    from app import app
    from app.pycaptive_settings import HOST, PORT
    print("\n --------------------------------------------")
    print("\n PyCaptive Standalone Mode\n")
    print(" \033[1;34mINFO\033[1;m: I was designed for test purposes only.\n")
    print(" -------------------------------------------- \n")
    try:
        app.run(host=HOST, port=PORT)
    except KeyboardInterrupt:
        print("Interrupted!")
    except Exception as e:
        print("Exception:", e)
