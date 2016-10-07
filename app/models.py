from app import db


student_subject = db.Table('student_subject', db.metadata,
	db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
	db.Column('subject_id', db.Integer, db.ForeignKey('subject.id')),
	db.Column('grade_id', db.Integer, db.ForeignKey('grade.id')))


subject_teacher = db.Table('subject_teacher', db.metadata,
	db.Column('subject_id', db.Integer, db.ForeignKey('subject.id')),
	db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id')))


class Student(db.Model):
	__tablename__ = 'student'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(180), index = True)
	middle_name = db.Column(db.String(180), index = True)
	last_name = db.Column(db.String(180), index = True)
	gender = db.Column(db.String(6), index = True)
	grade_level = db.Column(db.Integer, index = True)
	mother_tongue = db.Column(db.String(50))
	info = db.relationship('StudentInfo', uselist = False, back_populates = 'student')
	parents = db.relationship('StudentParents', uselist = False, back_populates = 'student') 
	address = db.relationship('StudentAddress', uselist = False, back_populates = 'student') 
	grades = db.relationship('Grade', secondary=student_subject, back_populates='student') 

	# def __repr__(self):
	# 	return '<Category %r>' % self.name


class StudentInfo(db.Model):
	__table_name = 'student_info'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	ethnic_group = db.Column(db.String(50))
	religion = db.Column(db.String(50))
	student = db.relationship('Student', back_populates='info')


class StudentParents(db.Model):
	__table_name = 'student_parents'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	father_name = db.Column(db.String(50))
	mother_name = db.Column(db.String(50))
	student = db.relationship('Student', back_populates='parents')


class StudentAddress(db.Model):
	__table_name = 'student_address'
	id = db.Column(db.Integer, primary_key = True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	street = db.Column(db.String(50), index = True)
	barangay = db.Column(db.String(50), index = True)
	municipality = db.Column(db.String(50), index = True)
	province = db.Column(db.String(50), index = True)
	student = db.relationship('Student', back_populates='address')



class Teacher(db.Model):
	__tablename__ = 'teacher'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(180), index = True)
	middle_name = db.Column(db.String(180), index = True)
	last_name = db.Column(db.String(180), index = True)
	address = db.Column(db.Text)
	subjects = db.relationship("Subject", secondary=subject_teacher, back_populates='teachers')


class Subject(db.Model):
	__tablename__ = 'subject'
	id = db.Column(db.Integer, primary_key = True)
	subject_code = db.Column(db.String(60), index = True)
	subject_name = db.Column(db.String(60), index = True)
	teachers = db.relationship('Teacher', secondary=subject_teacher, back_populates='subjects')
	schedule = db.relationship('Schedule', back_populates='subject')


class Schedule(db.Model):
	__table_name = 'schedule'
	id = db.Column(db.Integer, primary_key = True)
	subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
	father_name = db.Column(db.String(50))
	mother_name = db.Column(db.String(50))
	subject = db.relationship('Subject', back_populates='schedule', uselist = False)



class Grade(db.Model):
	__tablename__ = 'grade'
	id = db.Column(db.Integer, primary_key = True)
	first_term = db.Column(db.Integer)
	second_term = db.Column(db.Integer)
	third_term = db.Column(db.Integer)
	fourth_term = db.Column(db.Integer)
	student = db.relationship("Student", secondary=subject_teacher, back_populates='teachers')


# Relationship association table definitions



