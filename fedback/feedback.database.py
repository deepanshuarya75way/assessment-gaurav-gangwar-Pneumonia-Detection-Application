import sqlite3 
from pathlib import path

BASE_DIR = path(__file__).resolve().parant
DB_PATH = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite.row_factoru

def initialize_database():
  connection = get_connection()

  connection.execute(
    """
    CREATE TABLE IF NOT EXISTS FEEDBACK (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    image_name TEXT,
    iamge_path TEXT,
    
    model_prediction Text not null
    
    corrected_label text,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    reviwed-at timestamp
    )
    """

  )

  connection.commit()
  connection.close()

  def save_feedback(
    image_nam,
    iamge_path,
    model_prediction,
    model_confidance,
    user_correct,
    corrected_label,
    status_code
  )
VALUES(?,?,?,?,?,?,'PENDING')
"",
(
  image_nam,
    iamge_path,
    model_prediction,
    model_confidance,
    user_correct,
    corrected_label,
),

connection.commit()
 feedback_id = cursor.lastwid
 connection.close()
  rows = connection.execute(
    """
    SELECT*
    from feedback WHERE STATUS = 'PENDING'



  ) 
  def_approve.feedback(feedback_id):
  connection = get_connection()

  connection.execute(
  """
  )
  
def_reject.feedback(feedback_id):
  connection = get_connection()

  connection.execute(
    """
    UPDATE FEEDBACK
    SET status = 'REJECTED'
        reviwed_at= CURRENT_TIMESTAMP

    WHERE id=?
    """,
    (feedback_id,)    



  )

  connection.commit()
  connection.close()