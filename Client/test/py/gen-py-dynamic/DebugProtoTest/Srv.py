#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.protocol.TBase import TBase, TExceptionBase, TTransport


class Iface(object):
  def Janky(self, arg):
    """
    Parameters:
     - arg
    """
    pass

  def voidMethod(self):
    pass

  def primitiveMethod(self):
    pass

  def structMethod(self):
    pass

  def methodWithDefaultArgs(self, something):
    """
    Parameters:
     - something
    """
    pass

  def onewayMethod(self):
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def Janky(self, arg):
    """
    Parameters:
     - arg
    """
    self.send_Janky(arg)
    return self.recv_Janky()

  def send_Janky(self, arg):
    self._oprot.writeMessageBegin('Janky', TMessageType.CALL, self._seqid)
    args = Janky_args()
    args.arg = arg
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_Janky(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = Janky_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "Janky failed: unknown result")

  def voidMethod(self):
    self.send_voidMethod()
    self.recv_voidMethod()

  def send_voidMethod(self):
    self._oprot.writeMessageBegin('voidMethod', TMessageType.CALL, self._seqid)
    args = voidMethod_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_voidMethod(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = voidMethod_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def primitiveMethod(self):
    self.send_primitiveMethod()
    return self.recv_primitiveMethod()

  def send_primitiveMethod(self):
    self._oprot.writeMessageBegin('primitiveMethod', TMessageType.CALL, self._seqid)
    args = primitiveMethod_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_primitiveMethod(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = primitiveMethod_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "primitiveMethod failed: unknown result")

  def structMethod(self):
    self.send_structMethod()
    return self.recv_structMethod()

  def send_structMethod(self):
    self._oprot.writeMessageBegin('structMethod', TMessageType.CALL, self._seqid)
    args = structMethod_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_structMethod(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = structMethod_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "structMethod failed: unknown result")

  def methodWithDefaultArgs(self, something):
    """
    Parameters:
     - something
    """
    self.send_methodWithDefaultArgs(something)
    self.recv_methodWithDefaultArgs()

  def send_methodWithDefaultArgs(self, something):
    self._oprot.writeMessageBegin('methodWithDefaultArgs', TMessageType.CALL, self._seqid)
    args = methodWithDefaultArgs_args()
    args.something = something
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_methodWithDefaultArgs(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = methodWithDefaultArgs_result()
    result.read(iprot)
    iprot.readMessageEnd()
    return

  def onewayMethod(self):
    self.send_onewayMethod()

  def send_onewayMethod(self):
    self._oprot.writeMessageBegin('onewayMethod', TMessageType.ONEWAY, self._seqid)
    args = onewayMethod_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["Janky"] = Processor.process_Janky
    self._processMap["voidMethod"] = Processor.process_voidMethod
    self._processMap["primitiveMethod"] = Processor.process_primitiveMethod
    self._processMap["structMethod"] = Processor.process_structMethod
    self._processMap["methodWithDefaultArgs"] = Processor.process_methodWithDefaultArgs
    self._processMap["onewayMethod"] = Processor.process_onewayMethod

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_Janky(self, seqid, iprot, oprot):
    args = Janky_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = Janky_result()
    try:
      result.success = self._handler.Janky(args.arg)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("Janky", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_voidMethod(self, seqid, iprot, oprot):
    args = voidMethod_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = voidMethod_result()
    try:
      self._handler.voidMethod()
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("voidMethod", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_primitiveMethod(self, seqid, iprot, oprot):
    args = primitiveMethod_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = primitiveMethod_result()
    try:
      result.success = self._handler.primitiveMethod()
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("primitiveMethod", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_structMethod(self, seqid, iprot, oprot):
    args = structMethod_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = structMethod_result()
    try:
      result.success = self._handler.structMethod()
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("structMethod", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_methodWithDefaultArgs(self, seqid, iprot, oprot):
    args = methodWithDefaultArgs_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = methodWithDefaultArgs_result()
    try:
      self._handler.methodWithDefaultArgs(args.something)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("methodWithDefaultArgs", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_onewayMethod(self, seqid, iprot, oprot):
    args = onewayMethod_args()
    args.read(iprot)
    iprot.readMessageEnd()
    try:
      self._handler.onewayMethod()
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except:
      pass


# HELPER FUNCTIONS AND STRUCTURES

class Janky_args(TBase):
  """
  Attributes:
   - arg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'arg', None, None, ), # 1
  )

  def __init__(self, arg=None,):
    self.arg = arg

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.arg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Janky_result(TBase):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class voidMethod_args(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class voidMethod_result(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class primitiveMethod_args(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class primitiveMethod_result(TBase):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class structMethod_args(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class structMethod_result(TBase):
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (CompactProtoTestStruct, CompactProtoTestStruct.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class methodWithDefaultArgs_args(TBase):
  """
  Attributes:
   - something
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'something', None, 2, ), # 1
  )

  def __init__(self, something=thrift_spec[1][4],):
    self.something = something

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.something)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class methodWithDefaultArgs_result(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class onewayMethod_args(TBase):

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
