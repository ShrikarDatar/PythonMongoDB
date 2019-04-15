from flask import Flask, jsonify ,url_for, request
from flask.ext.pymongo import PyMongo
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myData"]
mycol = mydb["users"]

#index page for inserting the documents in the collection

@app.route('/')
def index():
        return '''
            <form method = "POST" action = "/create" >
                name: <input type="text" name="name"><br><br>
                language: <input type="text" name="language"><br><br>
                <input type="submit" name="create">
            </form>
        '''


@app.route('/create', methods=['POST'])
def create():
    mycol.insert_one({'name':request.form.get('name'),'language':request.form.get('language')})
    return 'Successfully added user'


#Updation of data in the documents

@app.route('/update')
def update():
    return '''
            <form method = "POST" action = "/modify">
                name: <input type="text" name="name"><br><br>
                New Name: <input type="text" name="newName"><br><br>
                <input type="submit" name="find">
            </form>
        '''


@app.route('/modify', methods=['POST'])
def modify():
    name = str(request.form.get('name'))
    newName = str(request.form.get('newName'))
    f = mycol.update_one({'name':name},{"$set" : {'name': newName}})
    return 'Updated successfully'


#finding the single document in the collection

@app.route('/find')
def find():
    return '''
            <form method = "POST" action = "/search">
                name: <input type="text" name="name"><br><br>
                <input type="submit" name="find">
            </form>
        '''

@app.route('/search', methods=['POST'])
def search():
    myName = str(request.form.get('name'))
    result = mycol.find({'name':myName})

    output = ''
    for r in result:
        output = r['name'] + '<br>'
    return 'You found '+output +'Your favorite language is '+r['language']


#deletion of document in the collection 

@app.route('/delete')
def delete():
    return'''
            <form method = "POST" action = "/remove">
                name: <input type="text" name="name"><br><br>
                <input type="submit" name="find">
            </form>      
        '''


@app.route('/remove',methods =['POST'])
def remove():
    name = str(request.form.get('name'))
    f = mycol.remove({'name':name})
    return 'Deleted successfully'


#displaying the documents in the collection

@app.route('/findall',methods =['GET'])
def findall():
    framework = mycol
    output = []

    for q in framework.find():
        output.append({'name':q['name'],'language':q['language']})

    return jsonify({'result': output})


#displaying the sorted documents in the collection

@app.route('/sort')
def sort():
    users = mycol
    result = users.find().sort('name', pymongo.ASCENDING)

    output = ''
    for r in result:
        output += r['name']+ '<br>'
    return output



#sorting of document in the collection with limits 

@app.route('/sortlimit')
def sortlimit():
    return'''
            <form method = "POST" action = "/limit">
                Enter the limit for sort: <input type="text" name="name">
                <input type="submit" name="find">
            </form>
        '''


@app.route('/limit',methods =['POST'])
def limit():
    limits = int(request.form.get('name'))
    users = mycol
    result = users.find().limit(limits).sort('name', pymongo.ASCENDING)

    output = ''
    for r in result:
        output += r['name']+ '<br>'
    return output




    
@app.route('/upload')
def upload():
    return'''
            <form method = "POST" action = "/image" enctype"multipart/form-data">
                <input type="text" name="username">
                <input type="file" name="profile_image">
                <input type="submit">
            </form>
        '''


@app.route('/image',methods =['POST'])
def image():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mycol.save_file(profile_image.filename, profile_image)
        mycol.insert_one({'username':request.form.get('username'),'profile_image_name':profile_image.filename})
    return 'done!'

@app.route('/file/<filename>')
def file(filename):
    return mycol.send_file(filename)



if __name__ == '__main__':
    app.run(debug=True)
