#!/usr/local/munki/munki-python
'''Return a list of entra groups for the JAMF enrolled user'''

from __future__ import absolute_import, print_function

import os
import sys

sys.path.append('/usr/local/munki')
try:
    from munkilib import FoundationPlist
except ImportError:
    print('ERROR: Cannot import FoundationPlist')
    sys.exit(1)


def fact():
    '''Return the list of entra groups for the JAMF enrolled user'''
    return {'jamf_tags': get_jamf_tags()}

def get_jamf_tags():
    """Read groups from /usr/local/matw/config/tags.plist."""
    # target = 'Display Menu'
    tag_list_dir = '/usr/local/matw/config'
    tag_list_name = 'tags'
    tag_list_path = f'{tag_list_dir}/{tag_list_name}.plist'

    if os.path.exists(tag_list_path):
        try:
            tags_plist =  FoundationPlist.readPlist(tag_list_path)
        except FoundationPlist.NSPropertyListSerializationException:
            print(f'ERROR: Cannot read {tag_list_path}')
            sys.exit(1)

        try:
            jamf_tags = list(tags_plist['jamf_tags'])
            return(jamf_tags)
        except KeyError:
            pass
        
    return([])


if __name__ == '__main__':
    print(fact())













#!/usr/local/munki/munki-python




