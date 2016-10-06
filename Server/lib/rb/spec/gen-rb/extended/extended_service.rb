#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

require 'thrift'
require 'base/base_service'
require 'extended/extended_service_types'

module Extended
  module ExtendedService
    class Client < ::Base::BaseService::Client 
      include ::Thrift::Client

      def ping()
        send_ping()
        recv_ping()
      end

      def send_ping()
        send_message('ping', Ping_args)
      end

      def recv_ping()
        result = receive_message(Ping_result)
        return
      end

    end

    class Processor < ::Base::BaseService::Processor 
      include ::Thrift::Processor

      def process_ping(seqid, iprot, oprot)
        args = read_args(iprot, Ping_args)
        result = Ping_result.new()
        @handler.ping()
        write_result(result, oprot, 'ping', seqid)
      end

    end

    # HELPER FUNCTIONS AND STRUCTURES

    class Ping_args
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class Ping_result
      include ::Thrift::Struct, ::Thrift::Struct_Union

      FIELDS = {

      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

  end

end
