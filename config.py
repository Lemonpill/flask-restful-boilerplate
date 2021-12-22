class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RATELIMIT_DEFAULT = "60/minute"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_HEADER_RETRY_AFTER_VALUE = "delta-seconds"
    

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = "5eqjsbtULffh?4N@53M3LdxBBHPQS*vFQebrLf9S&S6?EA_LY7!kH&5eqC8+ZL72cpHURuH5Gh3t2uPrxPmCV@9AGS@mLW*D^KuD^?bHhDRbQL#8^T?YLFvezMF!jh+GFmE-x+ab#8Wdy=!k2Duc=KsrP?MPh3u#UE9F5RBY^2g2Naq9fbLG^?2HjkfGUU?&$4AhVk?_Z3GN*^y@ddxy9-xB#S&nHbAwG3G&h82!VARA9yD488mFZ35!5LuPU54BUa@D6HaCGx$TGF3Hm9#6@Ku^X3Qd%Q+sBmZgmsK5cfc9axP^=f?NhGRcsuABRW-5A?hN&NGLVsHUgQqN$93UVwNk56276BfjHrmLtDUx4unJ7_M7uEP*h9qchXTJKxKPRe+g6JgVgdu5a??629k%?E-s-gBAn-GFr4b@%yhhYzH+@%R#U3FnDzb^XL-Qu=DQGD^aQMx=Yf7a89tSTLFpZHu?=puwYhqY$B!k%M=T49AYaufZ!SgKTSCy22Ff_-z"
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = '0DRfpTmR1Qd1Nv4kVJ8cjI0VSLnf1QV5LsnNRTFDkBwmDfHVjUQJMz08Nfty084M'
    DEBUG = True

class TestingConfig(Config):
    TESTING = True