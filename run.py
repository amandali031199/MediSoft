from routes import app,system, AppointmentSystem
from Database import *
import os

if __name__ == '__main__':
    # SIGINT to stop (Ctrl + C)
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=5151)
    
    #save data
    print("Saving...")
    #system.save_data()
    AppointmentSystem.save_data()
