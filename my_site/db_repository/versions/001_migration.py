from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
names = Table('names', pre_meta,
    Column('name', VARCHAR(length=30)),
)

useless_words = Table('useless_words', pre_meta,
    Column('word', VARCHAR(length=30)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['names'].drop()
    pre_meta.tables['useless_words'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['names'].create()
    pre_meta.tables['useless_words'].create()
