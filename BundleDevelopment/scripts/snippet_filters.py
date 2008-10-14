###############################################################################

import re

###############################################################################
"""

All callables with prefix of filter_ will be applied to snippets

Callables will be passed 3 arguments:

    content     =>  The snippet content
    plist_dict  =>  The snippet plist as a python dict 
    bundle      =>  `xxxxx.tmBundle`

You can name the 3 variables whatever you like but they must be in that order

If no filtering is done just return None (implicit with no return)

"""

INTERPOLATIONS_RE = re.compile(r"`([^`\\]|\\`|\\)+`")

def filter_ruby_snippet_paren_rb(content, _, bundle):
    if bundle is 'Ruby.tmBundle':
        s = content.replace('`snippet_paren.rb end`', ')')
        return s.replace('`snippet_paren.rb`', '(')


def dont_filter_log_interpolations(content, plist_dict, bundle):
    m = INTERPOLATIONS_RE.search(content)
    if m: print bundle, content[slice(*m.span())]

def filter_last_tabstops(content, plist_dict, bundle):
    """

    $0 placeholder used to denote `last` tabstop in TM. In Sublime the last
    tabstop is the highest one.

    """

    s = re.sub(r"(?:\$\{|\$)0", lambda l: l.group(0).replace('0', '15'), content)
    return s

###############################################################################

if __name__ == '__main__':
    test = r"""
      `   
      if [[ arstarst ]] if:
        \`   \` \e
      
      end
      `  
  
    """
    
    print test[slice(*INTERPOLATIONS_RE.search(test).span())]