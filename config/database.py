from deta import Deta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

deta = Deta()
database = deta.Base('urls')