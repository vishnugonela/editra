###############################################################################
#    Copyright (C) 2007 Cody Precord                                          #
#    staff@editra.org                                                         #
#                                                                             #
#    Editra is free software; you can redistribute it and#or modify           #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation; either version 2 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    Editra is distributed in the hope that it will be useful,                #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program; if not, write to the                            #
#    Free Software Foundation, Inc.,                                          #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.                #
###############################################################################

"""
#-----------------------------------------------------------------------------#
# FILE: smalltalk.py                                                          #
# AUTHOR: Cody Precord                                                        #
#                                                                             #
# SUMMARY:                                                                    #
# Lexer configuration module for Smalltalk                                    #
#                                                                             #
# TODO: more keywords, styling fixes                                          #
#                                                                             #
#-----------------------------------------------------------------------------#
"""

__author__ = "Cody Precord <cprecord@editra.org>"
__svnid__ = "$Id$"
__revision__ = "$Revision$"

#-----------------------------------------------------------------------------#

#---- Keyword Definitions ----#
# Special Selectors
st_keywords = (0, "ifTrue: ifFalse: whileTrue: whileFalse: ifNil: ifNotNil: "
                  "whileTrue repeat isNil put to at notNil super self "
                  "true false new not isNil inspect out nil do add for "
                  "methods methodsFor instanceVariableNames classVariableNames "
                  "poolDictionaries subclass")
#---- End Keyword Definitions ----#

#---- Syntax Style Specs ----#
syntax_items = [('STC_ST_ASSIGN', 'operator_style'),
                ('STC_ST_BINARY', 'operator_style'),
                ('STC_ST_BOOL', 'keyword_style'),
                ('STC_ST_CHARACTER', 'char_style'),
                ('STC_ST_COMMENT', 'comment_style'),
                ('STC_ST_DEFAULT', 'default_style'),
                ('STC_ST_GLOBAL', 'global_style'),
                ('STC_ST_KWSEND', 'keyword_style'),
                ('STC_ST_NIL', 'keyword_style'),
                ('STC_ST_NUMBER', 'number_style'),
                ('STC_ST_RETURN', 'keyword_style'),
                ('STC_ST_SELF', 'keyword_style'),
                ('STC_ST_SPECIAL', 'pre_style'),
                ('STC_ST_SPEC_SEL', 'keyword_style'),   # Words in keyword list
                ('STC_ST_STRING', 'string_style'),
                ('STC_ST_SUPER', 'class_style'),
                ('STC_ST_SYMBOL', 'scalar_style')]

#---- Extra Properties ----#

#-----------------------------------------------------------------------------#

#---- Required Module Functions ----#
def Keywords(langId=0):
    """Returns Specified Keywords List
    @param langId: used to select specific subset of keywords

    """
    return [st_keywords]

def SyntaxSpec(langId=0):
    """Syntax Specifications
    @param langId: used for selecting a specific subset of syntax specs

    """
    return syntax_items

def Properties(langId=0):
    """Returns a list of Extra Properties to set
    @param langId: used to select a specific set of properties

    """
    return list()

def CommentPattern(langId=0):
    """Returns a list of characters used to comment a block of code
    @param langId: used to select a specific subset of comment pattern(s)

    """
    return [u'\"', u'\"']
#---- End Required Module Functions ----#

#---- Syntax Modules Internal Functions ----#
def KeywordString():
    """Returns the specified Keyword String
    @note: not used by most modules

    """
    return st_keywords[1]

#---- End Syntax Modules Internal Functions ----#
