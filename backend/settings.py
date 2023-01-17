from split_settings.tools import include

include(
    'components/auth.py',
    'components/base.py',
    'components/database.py',
    'envs/development.py', # For development (TRUE)
    # 'envs/production.py', # For Production (FALSE)
    
)
