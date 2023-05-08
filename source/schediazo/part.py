""" Part base classes
"""
from __future__ import annotations
from typing import List, Union, Iterable
import xml.etree.ElementTree as ET
import uuid
import base64


def generate_id() -> str:
    """Generate a random ID string for an element.

    Returns
    -------
    str
        String representation of a random id.
    """
    id_bytes = uuid.uuid4().bytes
    id = base64.b64encode(id_bytes, altchars=bytes('-_',encoding='ascii'))
    return 's'+str(id.replace(b'=',b''),encoding='ascii')



class PartBase:
    """Base class for part of a drawing.
    """
    def __init__(self, id: str=None, **kwargs):
        """Initialise

        Parameters
        ----------
        id : str, optional
            An ID for this part.
        """
        self._tag = None
        if id is None:
            self._id = generate_id()
        else:
            self._id = id

    @property
    def id(self):
        return self._id

    def __repr__(self) -> str:
        return 'PartBase({})'.format(self._id)

    def create_element(self, root: Union[ET.Element,ET.SubElement]) -> ET.SubElement:
        """Create the XML element

        Parameters
        ----------
        root : Union[ET.Element,ET.SubElement]
            XML Element to create this new element under.

        Returns
        -------
        ET.SubElement
            Created XML element.
        """
        element = ET.SubElement(root, self._tag)
        self.set_element_attributes(element)
        return element

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to set the attributes in.
        """
        element.set('id', self._id)



class _DoublyLinkedListNode:
    """Node for a doubly-linked list

    Attributes
    ----------
    prev : str
        Key for the previous node.
    next : str
        Key for the next node.
    key : str
        Key for this node.
    """
    __slots__ = 'prev', 'next', 'key'

    def __repr__(self) -> str:
        """Generate a string representation of this list node

        Returns
        -------
        str
            String representation
        """
        return 'Node(prev={}, next={}, key={})'.format(self.prev, self.next, self.key)



class PartDict(dict):
    """Ordered dictionary of Parts
    """

    def __init__(self, id: str=None):
        """Initialise.

        Parameters
        ----------
        id : str, optional
            An ID for this part.
        """
        self.__map = {}         # Store the nodes _DoublyLinkedListNode.
        self.__head = None      # Key for the head node.
        self.__tail = None      # Key for the tail node.

        self._tag = None
        if id is None:
            self._id = generate_id()
        else:
            self._id = id

    @property
    def id(self):
        return self._id

    def add(self, part: Union[PartBase,PartDict]):
        """Add a part.

        Parameters
        ----------
        part : Union[PartBase,PartDict]
            The part to add
        """
        self[part.id] = part

    def create_element(self, root: Union[ET.Element,ET.SubElement]) -> ET.SubElement:
        """Create the XML element and all the child elements.

        Parameters
        ----------
        root : Union[ET.Element,ET.SubElement]
            XML Element to create this new element under.

        Returns
        -------
        ET.SubElement
            Created XML element.
        """
        element = ET.SubElement(root, self._tag)
        self.set_element_attributes(element)
        for child in self:
            self[child].create_element(element)
        return element

    def set_element_attributes(self, element: Union[ET.SubElement,ET.Element]):
        """Set the SVG element attributes.

        Parameters
        ----------
        element : Union[ET.SubElement,ET.Element]
            Element to set the attributes in.
        """
        element.set('id', self._id)

    def __setitem__(self, key: str, value: Union[PartBase,PartDict]):
        """Insert a new part - this will be added to the tail (front)

        Parameters
        ----------
        key : str
            Id for this Part.
        value : Union[PartBase,PartDict]
            Part object.

        Raises
        ------
        TypeError
            If the object is not a Part (or derived from PartBase)
        """
        if not isinstance(value, (PartBase,PartDict)):
            raise TypeError

        # If the key doesn't already exist then we need to add it to the list.
        if key not in self:
            self._list_insert_tail(key)
        dict.__setitem__(self, key, value)

    def __iter__(self) -> str:
        """Iterate over the keys from back to front.

        Yields
        ------
        str
            Id.
        """
        current = self.__head
        while current is not None:
            yield current
            current = self.__map[current].next

    def __reversed__(self) -> str:
        """Iterate over the keys from front to back

        Yields
        ------
        str
            Id
        """
        current = self.__tail
        while current is not None:
            yield current
            current = self.__map[current].prev

    def __delitem__(self, key: str):
        """Delete an item from this container.

        Parameters
        ----------
        key : str
            Id
        """
        dict.__delitem__(self, key)
        self._list_remove(key)

    def clear(self):
        """Empty the container.
        """
        self.__head = None
        self.__tail = None
        self.__map.clear()
        dict.clear(self)

    def movetofront(self, key: str):
        """Move a part to the front.

        Parameters
        ----------
        key : str
            Id.
        
        Raises
        ------
        KeyError
            If the id is not in the container.
        """
        
        if not (key in self.__map):
            raise KeyError

        self._list_movetotail(key)

    def movetoback(self, key: str):
        """Move a part to the back.

        Parameters
        ----------
        key : str
            Id.

        Raises
        ------
        KeyError
            If the id is not in the container.
        """
        if not (key in self.__map):
            raise KeyError

        self._list_movetohead(key)

    def moveforward(self, key: str):
        """Move part forward.

        Parameters
        ----------
        key : str
            Id.

        Raises
        ------
        KeyError
            If id is not in this container.
        """
        if not (key in self.__map):
            raise KeyError

        self._list_movetowardstail(key)

    def movebackward(self, key: str):
        """Move part backward.

        Parameters
        ----------
        key : str
            Id.

        Raises
        ------
        KeyError
            If id is not in this container.
        """
        if not (key in self.__map):
            raise KeyError

        self._list_movetowardshead(key)

    def _list_insert_tail(self, key: str):
        """Insert a key placing it at the tail of the list.

        Parameters
        ----------
        key : str
            Key to insert.
        """
        node = _DoublyLinkedListNode()

        if self.__head is None and self.__tail is None:
            # If this is the very first item we insert into the list 
            # then __tail=key, __head=key and the node should have
            # no next/prev keys.
            node.next, node.prev, node.key = None, None, key
            self.__tail = key
            self.__head = key
            self.__map[key] = node

        else:
            # We are appending a node to the tail.  We don't change the
            # __head but __tail=key.  The new node has next=None,
            # prev=the old __tail.  The old tail node has next=key,
            old_tail = self.__tail
            node.next, node.prev, node.key = None, old_tail, key
            self.__map[old_tail].next = key
            self.__tail = key
            self.__map[key] = node

    def _list_insert_head(self, key: str):
        """Insert a key placing it at the head of the list.

        Parameters
        ----------
        key : str
            Key to insert.
        """
        node = _DoublyLinkedListNode()

        if self.__head is None and self.__tail is None:
            # If this is the very first item we insert into the list 
            # then __tail=key, __head=key and the node should have
            # no next/prev keys.
            node.next, node.prev, node.key = None, None, key
            self.__tail = key
            self.__head = key
            self.__map[key] = node

        else:
            # We are appending a node to the head.  We don't change the
            # __tail but __head=key.  The new node has prev=None,
            # next=the old __head.  The old head node has prev=key,
            old_head = self.__head
            node.next, node.prev, node.key = old_head, None, key
            self.__map[old_head].prev = key
            self.__head = key
            self.__map[key] = node

    def _list_remove(self, key: str):
        """Remove an item from the list

        Parameters
        ----------
        key : str
            Key to remove from the list.

        Raises
        ------
        KeyError
            If the key is not in the list.
        """
        if not (key in self.__map):
            raise KeyError

        if self.__head is not None and self.__tail is not None:
            if len(self.__map)==1:
                # If there is only one item in the list then we just need to pop the
                # node from the map and set head/tail to None.
                self.__map.pop(key)
                self.__back = None
                self.__front = None

            else:
                # There's more than one item in the list.  Is it at the head?
                if self.__head==key:
                    # If this is at the head then the next node becomes the head,
                    # and the next node previous is set to None.
                    self.__head = self.__map[key].next
                    self.__map[self.__head].prev = None
                    self.__map.pop(key)

                elif self.__tail==key:
                    # If this is at the tail then the prev node becomes the tail,
                    # and the prev node next is set to None.
                    self.__tail = self.__map[key].prev
                    self.__map[self.__tail].next = None
                    self.__map.pop(key)

                else:
                    # The node is in the middle A-B-C, so we just need to get C's prev to point to A,
                    # and A's next to point to C.
                    link_prev = self.__map[key].prev
                    link_next = self.__map[key].next
                    self.__map[link_next].prev = link_prev
                    self.__map[link_prev].next = link_next
                    self.__map.pop(key)

    def _list_insert_after(self, key: str, after_key: str):
        """Insert an item into the list after a specific node.

        Parameters
        ----------
        key : str
            The key to insert.
        after_key : str
            The key for the node to insert after.

        Raises
        ------
        KeyError
            If the after key isn't in the list.
        """
        # Inserting an item before an after key.
        if not (after_key in self.__map):
            raise KeyError

        if len(self.__map)>1:
            # Possibilities: insert C after B: HEAD-A-B-TAIL to give HEAD-A-B-C-TAIL
            if self.__tail==after_key:
                self._list_insert_tail(key)

            else:
                # Possibilities: insert C after A: HEAD-A-B-TAIL to give HEAD-A-C-B-TAIL
                # in this case we insert between A and B.
                tailward_key = self.__map[after_key].next
                headward_key = after_key

                # A.next = key and B.prev = key
                self.__map[headward_key].next = key
                self.__map[tailward_key].prev = key
                node = _DoublyLinkedListNode()
                node.next, node.prev, node.key = tailward_key, headward_key, key
                self.__map[key] = node

    def _list_insert_before(self, key: str, before_key: str):
        """Insert an item into the list before a specific node.

        Parameters
        ----------
        key : str
            The key to insert.
        before_key : str
            The key for the node to insert before.

        Raises
        ------
        KeyError
            If the before key isn't in the list.
        """
        # Inserting an item before an existing key.
        if not (before_key in self.__map):
            raise KeyError

        if len(self.__map)>1:
            # Possibilities: insert C before A: HEAD - A - B - TAIL to give HEAD-C-A-B-TAIL
            if self.__head==before_key:
                self._list_insert_head(key)

            else:
                # Possibilities: insert C before B: HEAD - A - B - TAIL to give H-A-C-B-TAIL
                # in this case we insert between A and B.
                headward_key = self.__map[before_key].prev
                tailward_key = before_key

                # A.next = key and B.prev = key
                self.__map[headward_key].next = key
                self.__map[tailward_key].prev = key
                node = _DoublyLinkedListNode()
                node.next, node.prev, node.key = tailward_key, headward_key, key
                self.__map[key] = node

    def _list_movetohead(self, key: str):
        """Move a node in the list to the head of the list.

        Parameters
        ----------
        key : str
            Key to move.
        
        Raises
        ------
        KeyError
            If the key is not in the list.
        """
        if not (key in self.__map):
            raise KeyError

        if len(self.__map)>1 and not self.__head==key:
            # Only need to move to the head if there is more than one item.
            # Remove the item from the list and then insert into the head.
            self._list_remove(key)
            self._list_insert_head(key)

    def _list_movetotail(self, key: str):
        """Move a node in the list to the tail of the list.

        Parameters
        ----------
        key : str
            Key to move.
        
        Raises
        ------
        KeyError
            If the key is not in the list.
        """
        if not (key in self.__map):
            raise KeyError

        if len(self.__map)>1 and not self.__tail==key:
            # Only need to move to the tail if there is more than one item.
            # Remove the item from the list and then insert into the tail.
            self._list_remove(key)
            self._list_insert_tail(key)

    def _list_movetowardstail(self, key: str):
        """Move a node in the list towards the tail of the list.

        Parameters
        ----------
        key : str
            Key to move.
        
        Raises
        ------
        KeyError
            If the key is not in the list.
        """
        # If we are going to move B towards the tail: HEAD - A - B - C - TAIL
        # then we first remove the item to give HEAD - A - C - TAIL
        # then we insert after C to give HEAD - A - C - B - TAIL
        if not (key in self.__map):
            raise KeyError

        if len(self.__map)>1 and not self.__tail==key:
            # Only need to move towards the tail if there is more than one item.
            # Remove the item from the list and then insert after this key's next item.
            next = self.__map[key].next
            self._list_remove(key)
            self._list_insert_after(key, next)

    def _list_movetowardshead(self, key: str):
        """Move a node in the list towards the head of the list.

        Parameters
        ----------
        key : str
            Key to move.
        
        Raises
        ------
        KeyError
            If the key is not in the list.
        """
        # If we are going to move B towards the head: HEAD - A - B - C - TAIL
        # then we first remove the item to give HEAD - A - C - TAIL
        # then we insert before A to give HEAD - B - A - C - TAIL
        if not (key in self.__map):
            raise KeyError

        if len(self.__map)>1 and not self.__head==key:
            # Only need to move towards the head if there is more than one item.
            # Remove the item from the list and then insert before this key's prev item.
            prev = self.__map[key].prev
            self._list_remove(key)
            self._list_insert_before(key, prev)


