from flask import Flask,request,render_template,redirect,url_for
import mysql.connector

db={
    'host':'localhost',
    'user':'root',
    'password':'',          //write your mysql root password here
    'database':'Animal05'
}

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('AnimalHospital.html')

@app.route('/submit',methods=['POST','GET'])
def register():
    if request.method=='POST':
        animalType=request.form['animalType']
        animalBreed=request.form['animalBreed']
        age=request.form['age']
        email=request.form['email']
        phone=request.form['phone']
      

        try:
            conn=mysql.connector.connect(**db)
            cursor=conn.cursor()
            query="INSERT INTO Animal05.animals(animal_type,animal_breed,age,email,phone) VALUES (%s, %s,%s, %s,%s)"
            data=(animalType,animalBreed,age,email,phone)

            cursor.execute(query,data)

            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('details'))

        except Exception as e:
            return str(e)

        

@app.route('/register')
def details():
    try:
        conn=mysql.connector.connect(**db)
        cursor=conn.cursor()
        select_query="SELECT * FROM animals"
        cursor.execute(select_query)
        animal=cursor.fetchall()

        return render_template('animalRegistration.html',animal=animal)
    except Exception as e:
        return str(e)
    

if __name__=='__main__':
    app.run(debug=True)
