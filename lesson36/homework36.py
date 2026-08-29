from datetime import date
from sqlalchemy import create_engine, String, Integer, Float, ForeignKey, Date, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker, Session


DATABASE_URL = "postgresql+psycopg2://postgres:paroli@localhost:5432/hotel_db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass





class Hotel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    stars: Mapped[int] = mapped_column(Integer, nullable=False)

    rooms: Mapped[list["Room"]] = relationship("Room", back_populates="hotel", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Hotel(id={self.id}, name='{self.name}', city='{self.city}', stars={self.stars})>"


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    room_number: Mapped[str] = mapped_column(String(20), nullable=False)
    floor: Mapped[int] = mapped_column(Integer, nullable=False)
    price_per_night: Mapped[float] = mapped_column(Float, nullable=False)
    hotel_id: Mapped[int] = mapped_column(Integer, ForeignKey("hotels.id"), nullable=False)

    hotel: Mapped["Hotel"] = relationship("Hotel", back_populates="rooms")
    bookings: Mapped[list["Booking"]] = relationship("Booking", back_populates="room", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Room(id={self.id}, number='{self.room_number}', price={self.price_per_night})>"


class Guest(Base):
    __tablename__ = "guests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)

    bookings: Mapped[list["Booking"]] = relationship("Booking", back_populates="guest", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Guest(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')>"


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    guest_id: Mapped[int] = mapped_column(Integer, ForeignKey("guests.id"), nullable=False)
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey("rooms.id"), nullable=False)
    check_in: Mapped[date] = mapped_column(Date, nullable=False)
    check_out: Mapped[date] = mapped_column(Date, nullable=False)

    guest: Mapped["Guest"] = relationship("Guest", back_populates="bookings")
    room: Mapped["Room"] = relationship("Room", back_populates="bookings")

    def __repr__(self):
        return f"<Booking(id={self.id}, guest_id={self.guest_id}, room_id={self.room_id}, check_in={self.check_in}, check_out={self.check_out})>"





def create_hotel(session: Session, name: str, country: str, city: str, stars: int) -> Hotel:
    hotel = Hotel(name=name, country=country, city=city, stars=stars)
    session.add(hotel)
    session.commit()
    return hotel

def create_room(session: Session, room_number: str, floor: int, price_per_night: float, hotel_id: int) -> Room:
    room = Room(room_number=room_number, floor=floor, price_per_night=price_per_night, hotel_id=hotel_id)
    session.add(room)
    session.commit()
    return room

def create_guest(session: Session, first_name: str, last_name: str, email: str, phone: str) -> Guest:
    guest = Guest(first_name=first_name, last_name=last_name, email=email, phone=phone)
    session.add(guest)
    session.commit()
    return guest

def create_booking(session: Session, guest_id: int, room_id: int, check_in: date, check_out: date) -> Booking:
    booking = Booking(guest_id=guest_id, room_id=room_id, check_in=check_in, check_out=check_out)
    session.add(booking)
    session.commit()
    return booking


def get_all_hotels(session: Session) -> list[Hotel]:
    stmt = select(Hotel)
    return list(session.execute(stmt).scalars().all())

def get_hotel_by_id(session: Session, hotel_id: int) -> Hotel | None:
    return session.get(Hotel, hotel_id)

def get_all_rooms(session: Session) -> list[Room]:
    stmt = select(Room)
    return list(session.execute(stmt).scalars().all())

def get_guest_by_email(session: Session, email: str) -> Guest | None:
    stmt = select(Guest).where(Guest.email == email)
    return session.execute(stmt).scalars().first()


def update_room_price(session: Session, room_id: int, new_price: float) -> Room | None:
    room = session.get(Room, room_id)
    if room:
        room.price_per_night = new_price
        session.commit()
    return room


def delete_guest(session: Session, guest_id: int) -> None:
    guest = session.get(Guest, guest_id)
    if guest:
        session.delete(guest)
        session.commit()

def delete_room(session: Session, room_id: int) -> None:
    room = session.get(Room, room_id)
    if room:
        session.delete(room)
        session.commit()



def seed_database(session: Session) -> None:
    h1 = Hotel(name="Grand Hotel", country="Georgia", city="Tbilisi", stars=5)
    h2 = Hotel(name="Tbilisi Palace", country="Georgia", city="Tbilisi", stars=4)
    h3 = Hotel(name="Batumi Resort", country="Georgia", city="Batumi", stars=5)
    session.add_all([h1, h2, h3])
    session.commit()

    r1 = Room(room_number="101", floor=1, price_per_night=80.0, hotel=h1)
    r2 = Room(room_number="102", floor=1, price_per_night=120.0, hotel=h1)
    r3 = Room(room_number="201", floor=2, price_per_night=250.0, hotel=h1)

    r4 = Room(room_number="A1", floor=1, price_per_night=70.0, hotel=h2)
    r5 = Room(room_number="A2", floor=1, price_per_night=90.0, hotel=h2)
    r6 = Room(room_number="B1", floor=2, price_per_night=110.0, hotel=h2)

    r7 = Room(room_number="301", floor=3, price_per_night=150.0, hotel=h3)
    r8 = Room(room_number="302", floor=3, price_per_night=180.0, hotel=h3)
    r9 = Room(room_number="303", floor=3, price_per_night=95.0, hotel=h3)
    session.add_all([r1, r2, r3, r4, r5, r6, r7, r8, r9])
    session.commit()

    g1 = Guest(first_name="გიორგი", last_name="ბერიძე", email="giorgi@example.com", phone="599111111")
    g2 = Guest(first_name="ნიკო", last_name="კაპანაძე", email="niko@example.com", phone="599222222")
    g3 = Guest(first_name="ანა", last_name="მაისურაძე", email="ana@example.com", phone="599333333")
    g4 = Guest(first_name="დავით", last_name="გიორგაძე", email="davit@example.com", phone="599444444")
    g5 = Guest(first_name="ელენე", last_name="გელაშვილი", email="elene@example.com", phone="599555555")
    session.add_all([g1, g2, g3, g4, g5])
    session.commit()

    b1 = Booking(guest=g1, room=r1, check_in=date(2026, 5, 1), check_out=date(2026, 5, 5))
    b2 = Booking(guest=g1, room=r3, check_in=date(2026, 9, 10), check_out=date(2026, 9, 15))
    b3 = Booking(guest=g2, room=r2, check_in=date(2026, 6, 1), check_out=date(2026, 6, 4))
    b4 = Booking(guest=g2, room=r4, check_in=date(2026, 10, 1), check_out=date(2026, 10, 7))
    b5 = Booking(guest=g3, room=r5, check_in=date(2026, 7, 10), check_out=date(2026, 7, 12))
    b6 = Booking(guest=g4, room=r7, check_in=date(2026, 8, 15), check_out=date(2026, 8, 20))
    b7 = Booking(guest=g5, room=r9, check_in=date(2026, 11, 1), check_out=date(2026, 11, 5))
    session.add_all([b1, b2, b3, b4, b5, b6, b7])
    session.commit()



def run_queries(session: Session) -> None:
    print("==================================================")
    print("Query 1: ყველა 5-ვარსკვლავიანი სასტუმრო")
    print("==================================================")
    stmt1 = select(Hotel).where(Hotel.stars == 5)
    for hotel in session.execute(stmt1).scalars().all():
        print(hotel)

    print("\n==================================================")
    print("Query 2: თბილისში მდებარე სასტუმროები")
    print("==================================================")
    stmt2 = select(Hotel).where(Hotel.city == "Tbilisi")
    for hotel in session.execute(stmt2).scalars().all():
        print(hotel)

    print("\n==================================================")
    print("Query 3: ოთახები, რომელთა ფასი < 100")
    print("==================================================")
    stmt3 = select(Room).where(Room.price_per_night < 100)
    for room in session.execute(stmt3).scalars().all():
        print(room)

    print("\n==================================================")
    print("Query 4: ყველა ოთახი კონკრეტულ სასტუმროში (Relationship-ით)")
    print("==================================================")
    hotel = session.get(Hotel, 1)
    if hotel:
        print(f"სასტუმრო: {hotel.name}")
        for room in hotel.rooms:
            print(f"  - ოთახი: {room.room_number}, სართული: {room.floor}, ფასი: {room.price_per_night}")

    print("\n==================================================")
    print("Query 5: კონკრეტული სტუმრის ყველა Booking (Relationship-ით)")
    print("==================================================")
    guest = session.get(Guest, 1)
    if guest:
        print(f"სტუმარი: {guest.first_name} {guest.last_name}")
        for booking in guest.bookings:
            print(f"  - Booking #{booking.id}: ოთახი #{booking.room.room_number} ({booking.room.hotel.name}), {booking.check_in}-დან {booking.check_out}-მდე")

    print("\n==================================================")
    print("Query 6: ყველა Booking, რომლის check_out მომავალშია")
    print("==================================================")
    today = date.today()
    stmt6 = select(Booking).where(Booking.check_out > today)
    for b in session.execute(stmt6).scalars().all():
        print(f"Booking #{b.id}: სტუმარი {b.guest.first_name} {b.guest.last_name}, Check-out: {b.check_out}")

    print("\n==================================================")
    print("Query 7: ყველაზე ძვირი ოთახი")
    print("==================================================")
    stmt7 = select(Room).order_by(Room.price_per_night.desc())
    most_expensive = session.execute(stmt7).scalars().first()
    print(most_expensive)

    print("\n==================================================")
    print("Query 8: თითოეულ სასტუმროში ოთახების რაოდენობა (func.count)")
    print("==================================================")
    stmt8 = select(Hotel.name, func.count(Room.id)).join(Hotel.rooms).group_by(Hotel.id)
    for hotel_name, count in session.execute(stmt8).all():
        print(f"{hotel_name:<20} {count} rooms")

    print("\n==================================================")
    print("Query 9: ყველა სასტუმრო, რომელსაც აქვს მინიმუმ 3 ოთახი (group_by & having)")
    print("==================================================")
    stmt9 = select(Hotel).join(Hotel.rooms).group_by(Hotel.id).having(func.count(Room.id) >= 3)
    for hotel in session.execute(stmt9).scalars().all():
        print(hotel)

    print("\n==================================================")
    print("Query 10: სტუმრები, რომლებსაც 1-ზე მეტი Booking აქვთ")
    print("==================================================")
    stmt10 = select(Guest).join(Guest.bookings).group_by(Guest.id).having(func.count(Booking.id) > 1)
    for guest in session.execute(stmt10).scalars().all():
        print(guest)



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = SessionLocal()
try:
    seed_database(session)
    run_queries(session)
except Exception as e:
    session.rollback()
    print(f"დაფიქსირდა შეცდომა: {e}")
finally:
    session.close()