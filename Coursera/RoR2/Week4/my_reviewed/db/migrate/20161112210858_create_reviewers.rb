class CreateReviewers < ActiveRecord::Migration
  def change
    create_table :reviewers do |t|
      t.string :name
      t.string :password_digest

      t.timestamps null: false
    end
  end
end
