class Reviewer < ActiveRecord::Base
  
  has_secure_password

  has_many :books
end
