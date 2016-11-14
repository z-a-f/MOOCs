class CreateNotes < ActiveRecord::Migration
  def change
    create_table :notes do |t|
      t.string :title
      t.text :note
      t.references :book, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
