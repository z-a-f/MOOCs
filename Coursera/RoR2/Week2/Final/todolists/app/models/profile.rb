class Profile < ActiveRecord::Base
  belongs_to :user

  validate :permit_first_or_last_be_null
  validates :gender, inclusion: ["male", "female"]
  validate :male_cannot_be_sue

  def permit_first_or_last_be_null
  	if first_name == nil and last_name == nil
  		errors.add(:first_name, "Both first_name and last_name cannot be nil")
  	end
  end

  def male_cannot_be_sue
  	if gender == "male" and first_name == "Sue"
  		errors.add(:gender, "cannot be named Sue")
  	end
  end

  def self.get_all_profiles (min_birth_year, max_birth_year)
  	Profile
  		.where("birth_year BETWEEN :min_age AND :max_age", min_age: min_birth_year, max_age: max_birth_year)
  		.order("birth_year")
  		.to_a
  end
end
