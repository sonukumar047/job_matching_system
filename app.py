from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6')
db = client['job_matching_system']


# Entity1: Job Seeker Collection
job_seekers = db['job_seekers']

# Entity2: Job Posting Collection
job_postings = db['job_postings']

# Entity3: Application Collection
applications = db['applications']

# Entity4: Skill Set Collection
skill_sets = db['skill_sets']

# API endpoints for Job Seekers
@app.route('/jobseekers', methods=['GET'])
def get_all_job_seekers():
    result = list(job_seekers.find())

    for job_seeker in result:
        job_seeker['_id'] = str(job_seeker['_id'])
    
    return jsonify(result)

@app.route('/jobseekers', methods=['POST'])
def create_job_seeker():
    data = request.get_json()
    result = job_seekers.insert_one(data)
    return jsonify(str(result.inserted_id)), 201


@app.route('/jobseekers/<seeker_id>', methods=['GET'])
def get_job_seeker(seeker_id):
    job_seeker = job_seekers.find_one({'_id': ObjectId(seeker_id)})
    if job_seeker:
        job_seeker['_id'] = str(job_seeker['_id'])
        return jsonify(job_seeker)
    else:
        return jsonify({'error': 'Job seeker not found'}), 404

@app.route('/jobseekers/<seeker_id>', methods=['PUT'])
def update_job_seeker(seeker_id):
    data = request.get_json()
    result = job_seekers.update_one({'_id': ObjectId(seeker_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'Job seeker updated successfully'})
    else:
        return jsonify({'error': 'Job seeker not found'}), 404

@app.route('/jobseekers/<seeker_id>', methods=['DELETE'])
def delete_job_seeker(seeker_id):
    result = job_seekers.delete_one({'_id': ObjectId(seeker_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Job seeker deleted successfully'})
    else:
        return jsonify({'error': 'Job seeker not found'}), 404

# API endpoints for Job Postings
@app.route('/jobpostings', methods=['GET'])
def get_all_job_postings():
    result = list(job_postings.find())

    for job_posting in result:
        job_posting['_id'] = str(job_posting['_id'])
    
    return jsonify(result)

@app.route('/jobpostings', methods=['POST'])
def create_job_posting():
    data = request.get_json()
    data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
    data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')
    result = job_postings.insert_one(data)
    return jsonify(str(result.inserted_id)), 201

@app.route('/jobpostings/<job_id>', methods=['GET'])
def get_job_posting(job_id):
    job_posting = job_postings.find_one({'_id': ObjectId(job_id)})
    if job_posting:
        job_posting['_id'] = str(job_posting['_id'])
        return jsonify(job_posting)
    else:
        return jsonify({'error': 'Job posting not found'}), 404

@app.route('/jobpostings/<job_id>', methods=['PUT'])
def update_job_posting(job_id):
    data = request.get_json()

    if 'start_date' in data:
        data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')

    if 'end_date' in data:
        data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')

    result = job_postings.update_one({'_id': ObjectId(job_id)}, {'$set': data})
    
    if result.modified_count > 0:
        return jsonify({'message': 'Job posting updated successfully'})
    else:
        return jsonify({'error': 'Job posting not found'}), 404

@app.route('/jobpostings/<job_id>', methods=['DELETE'])
def delete_job_posting(job_id):
    result = job_postings.delete_one({'_id': ObjectId(job_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Job posting deleted successfully'})
    else:
        return jsonify({'error': 'Job posting not found'}), 404

# API endpoints for Applications
@app.route('/applications', methods=['GET'])
def get_all_applications():
    result = list(applications.find())

    for application in result:
        application['_id'] = str(application['_id'])
        application['job_posting'] = str(application['job_posting'])

    return jsonify(result)

@app.route('/applications', methods=['POST'])
def create_application():
    data = request.get_json()

    if 'job_posting' not in data:
        return jsonify({'error': 'Missing job_posting field'}), 400
    
    job_posting = db['job_postings'].find_one({'_id': ObjectId(data['job_posting'])})
    if not job_posting:
        return jsonify({'error': 'Job posting not found'}), 404

    data['job_posting'] = ObjectId(data['job_posting'])
    
    result = applications.insert_one(data)
    return jsonify(str(result.inserted_id)), 201

@app.route('/applications/<app_id>', methods=['GET'])
def get_application(app_id):
    application = applications.find_one({'_id': ObjectId(app_id)})
    if application:
        application['_id'] = str(application['_id'])
        application['job_posting'] = str(application['job_posting'])
        return jsonify(application)
    else:
        return jsonify({'error': 'Application not found'}), 404

@app.route('/applications/<app_id>', methods=['PUT'])
def update_application(app_id):
    data = request.get_json()
    result = applications.update_one({'_id': ObjectId(app_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'Application updated successfully'})
    else:
        return jsonify({'error': 'Application not found'}), 404

@app.route('/applications/<app_id>', methods=['DELETE'])
def delete_application(app_id):
    result = applications.delete_one({'_id': ObjectId(app_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Application deleted successfully'})
    else:
        return jsonify({'error': 'Application not found'}), 404

# Additional Features:

# Apply for a Job
@app.route('/jobpostings/<job_id>/apply', methods=['POST'])
def apply_for_job(job_id):
    job_posting = job_postings.find_one({'_id': ObjectId(job_id)})
    if job_posting:
        data = request.get_json()
        data['job_posting'] = job_id
        result = applications.insert_one(data)
        return jsonify(str(result.inserted_id)), 201
    else:
        return jsonify({'error': 'Job posting not found'}), 404

# API endpoints for Skill Sets
@app.route('/skillsets', methods=['GET'])
def get_all_skill_sets():
    result = list(skill_sets.find())

    for skill_set in result:
        skill_set['_id'] = str(skill_set['_id'])
        skill_set['job_posting'] = str(skill_set['job_posting'])

    return jsonify(result)

# Add Skill Set to a Job Posting
@app.route('/jobpostings/<job_id>/addskillset', methods=['POST'])
def add_skill_set_to_job(job_id):
    job_posting = job_postings.find_one({'_id': ObjectId(job_id)})
    if job_posting:
        data = request.get_json()
        data['job_posting'] = job_id
        result = skill_sets.insert_one(data)
        return jsonify(str(result.inserted_id)), 201
    else:
        return jsonify({'error': 'Job posting not found'}), 404



@app.route('/skillsets/<skill_set_id>', methods=['GET'])
def get_skill_set(skill_set_id):
    skill_set = skill_sets.find_one({'_id': ObjectId(skill_set_id)})
    if skill_set:
        skill_set['_id'] = str(skill_set['_id'])
        skill_set['job_posting'] = str(skill_set['job_posting'])
        return jsonify(skill_set)
    else:
        return jsonify({'error': 'Skill set not found'}), 404

@app.route('/skillsets/<skill_set_id>', methods=['PUT'])
def update_skill_set(skill_set_id):
    data = request.get_json()
    result = skill_sets.update_one({'_id': ObjectId(skill_set_id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'Skill set updated successfully'})
    else:
        return jsonify({'error': 'Skill set not found'}), 404

@app.route('/skillsets/<skill_set_id>', methods=['DELETE'])
def delete_skill_set(skill_set_id):
    result = skill_sets.delete_one({'_id': ObjectId(skill_set_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Skill set deleted successfully'})
    else:
        return jsonify({'error': 'Skill set not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)