from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask import Flask,render_template,request,jsonify,Response
import json
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
    jwt_required
)
# from models.country import Countries

# from models.user_new_version import User_newModel_version
from models.user_new import User_newModel
from db import db
from sqlalchemy_continuum import version_class


parser = reqparse.RequestParser()

parser.add_argument('name', type=str,required=True,
                    help="This field cannot be blank.")
parser.add_argument('email', type=str,required=True,
                    help="This field cannot be blank.")
parser.add_argument('mobile', type=int,required=True,
                    help="This field cannot be blank.")
parser.add_argument('country_id', type=int,required=True,
                    help="This field cannot be blank.")
parser.add_argument('state_id', type=int,required=True,
                    help="This field cannot be blank.")
parser.add_argument('city_id', type=int, required=True,
                    help="This field cannot be blank.")  
parser.add_argument('gender', type=int,required=True,
                    help="This field cannot be blank.")
parser.add_argument('hobbies', type=str,required=True,
                    help="This field cannot be blank.")
parser.add_argument('address', type=str,required=True,
                    help="This field cannot be blank.")
parser.add_argument('user_modified', type=str,required=True,
                    help="This field cannot be blank.")


class User_new(Resource):
    
    def get(self):
        users_list = User_newModel.query.all()
        users=[]
        # len=len(users_list)
        # print(users_list)
        for user in users_list:
            users.append({
                'id':user.id,
                'name':user.name,
                'email':user.email,
                'mobile':user.mobile,
                'country_id':user.country_id,
                'state_id':user.state_id,
                'city_id':user.city_id,
                'hobbies':user.hobbies,
                'gender':user.gender,
                'address':user.address
                
            })
            
            # print(users)
        return Response(json.dumps(users))

    # @jwt_required
    def post(self):
        args=parser.parse_args()
        if User_newModel.find_by_name(args['name']):
            return {"message": "A name with that name already exists"}, 400
        
        user = User_newModel(args['name'], args['email'], args['mobile'], args['country_id'], args['state_id'],args['city_id'],args['gender'], args['hobbies'], args['address'], args['user_modified'])
        user.save_to_db()
        return {'message': 'User Created'}, 200

class User_modify(Resource):

    def get(self, id):
        user = User_newModel.find_by_id(id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200

    
    # @jwt_required
    def put(self, id):
        args=parser.parse_args()
        user = User_newModel.find_by_id(id)
        
        name = args['name']
        email = args['email']
        mobile = args['mobile']
        country_id = args['country_id']
        state_id =  args['state_id']
        city_id = args['city_id']
        gender = args['gender']
        hobbies = args['hobbies'] 
        address = args['address']
        user_modified = args['user_modified']
       
        user.name = name
        user.email = email
        user.mobile = mobile
        user.country_id = country_id
        user.state_id = state_id
        user.city_id = city_id
        user.gender = gender
        user.hobbies = hobbies
        user.address = address
        user.user_modified = user_modified
        
        user.save_to_db()
        return {'message': 'User Updated'}, 200
    
    # @jwt_required
    def delete(self,id):
        user=User_newModel.find_by_id(id)
        user.delete_from_db()
        return {'message': 'User Deleted'}, 200


class User_new_v(Resource):
    def get(self):
        UserNewVersion = version_class(User_newModel)
        users_list = UserNewVersion.query.all()
        users=[]
        # len=len(users_list)
        # print(users_list)
        for user in users_list:
            users.append({
                'id':user.id,
                'name':user.name,
                'email':user.email,
                'mobile':user.mobile,
                'country_id':user.country_id,
                'state_id':user.state_id,
                'city_id':user.city_id,
                'hobbies':user.hobbies,
                'gender':user.gender,
                'address':user.address,
                'transaction_id':user.transaction_id,
                'end_transaction_id':user.end_transaction_id,
                'operation_type':user.operation_type,
                'user_modified':user.user_modified
                
            })
            
            # print(users)
        return Response(json.dumps(users))
    
    # def post(self):
 
    
    

  
       


 
  