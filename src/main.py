import uvicorn
import os
import sys

# Add the project root (/code) to sys.path
sys.path.append('/code')

from src.pred.image_classifier import *

if __name__ == "__main__":
    # even though uvicorn is running on 0.0.0.0 check 127.0.0.1 from the browser

    if "code" in os.getcwd():
        uvicorn.run("src.app.app:app", host="0.0.0.0", port=7001, log_level="debug",
                    proxy_headers=True, reload=True, reload_dirs=["src"])
    else:
        # for running locally from IDE without Docker
        uvicorn.run("src.app.app:app", host="0.0.0.0", port=7001, log_level="debug",
                    proxy_headers=True, reload=True, reload_dirs=["src"])