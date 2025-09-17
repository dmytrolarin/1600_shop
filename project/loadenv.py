import os, dotenv


PATH_ENV = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
PATH_MIGRATIONS = os.path.abspath(os.path.join(__file__, "..", "migrations"))

def load_env():
    dotenv.load_dotenv(dotenv_path= PATH_ENV)
    if not os.path.exists(PATH_MIGRATIONS):
        os.system(os.environ["DB_INIT"])
    os.system(os.environ["DB_MIGRATE"])
    os.system(os.environ["DB_UPGRADE"])