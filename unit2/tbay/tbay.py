from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://koji:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    auctioneer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_bid = relationship("Bid", backref="item")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    auctions = relationship("Item", backref="auctioneer")
    bids = relationship("Bid", backref="bidder")

class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)


Base.metadata.create_all(engine)

if __name__ == "__main__":
    aimee = User(username="anoble", password="l8blmr")
    melissa = User(username="mherrera", password="missylou")
    melinda = User(username="maragon", password="arcadia")
    session.add_all([aimee, melissa, melinda])
    session.commit()

    baseball = Item(name="baseball", description="toy", auctioneer=aimee)
    session.add(baseball)
    session.commit()

    melissa_bid1 = Bid(price=50, item=baseball, bidder=melissa)
    melinda_bid1 = Bid(price=55, item=baseball, bidder=melinda)
    melissa_bid2 = Bid(price=61, item=baseball, bidder=melissa)
    melinda_bid2 = Bid(price=72.1, item=baseball, bidder=melinda)
    session.add_all([melissa_bid1, melinda_bid1, melinda_bid2, melissa_bid2])
    session.commit()

    highest_bid = session.query(Bid).order_by(desc(Bid.price)).first()
    winner = highest_bid.bidder.username
    won_price = highest_bid.price

    print("The winner is: ", winner)
    print("Final price is ", won_price, "dollar.")
