from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="birthday",
    size="large",
    rating=5,
    image="https://t3.ftcdn.net/jpg/06/05/76/12/240_F_605761275_O3LOdFUNaHm1ZUz9qZGnvLCWUU5tZK4L.jpg"
)

c2 = Cupcake(
    flavor="strawberry",
    size="small",
    rating=9,
    image="https://t3.ftcdn.net/jpg/06/42/62/24/240_F_642622462_WrtxLM7FLDn3VWfFmXyI6lvzEKU2VgqH.jpg"
)

db.session.add_all([c1, c2])
db.session.commit()
