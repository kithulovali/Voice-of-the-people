### server side implimentation , installation and contribution design .

<h3>Installation</h3>
<hr>
Clone the remote repositorie to your local computer .
git clone 
<hr>
 <h3>Downlaod the python interpriter</h3> 
 
 [Python](https://www.python.org/downloads/)
 Python version used 3.13.5

 <hr>

 <h3> Create a virtual environment</h3> 

 
 '''
 python -m venv .venv  # windows
 ''' 
 <br>
 """
 python3 -m venv .venv  # linux , Macos
 """

 <h3>Activate the virtual environment</h3>
 """ source .venv/Scripts/activate  # windows """
 <br>
 """ source .venv/bin/activate      # Linux , Macos """

 <h3>Used libraries</h3>
 <ul>
   <li>sqlalchemy</li>
   <li>fastapi</li>
 </ul>

 <h3>Install the required packages<h3> 

 """ pip install fastapi[standard] sqlalchemy """
