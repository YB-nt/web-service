import pynecone as pc

class ApplicationConfig(pc.Config):
    pass

config = ApplicationConfig(
    app_name="Application",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=3000
)