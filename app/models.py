from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, nullable=False)
    userName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    isArchive = Column(Boolean, default=False)
    createTime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    

class Info(Base):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True, nullable=False, comment='序號')
    deviceName = Column(String(60), nullable=False, comment='裝置名稱')
    power = Column(Integer, nullable=True, comment='手錶電量%')
    trackingModeColor = Column(String(60), nullable=True, comment='定位頻率對應色碼')
    connected = Column(String(1), nullable=False, comment='是否連線：Y | N')
    connectStatus = Column(String(20), nullable=False, comment='連線狀態：onLine | offLine')
    step = Column(Integer, nullable=True, comment='時間區段內計步量')
    lockMode = Column(String(1), nullable=False, comment='是否在上鎖模式：Y|N')
    
    def __repr__(self):
        return f"<Device(deviceName={self.deviceName}, power={self.power}, connected={self.connected})>"
    