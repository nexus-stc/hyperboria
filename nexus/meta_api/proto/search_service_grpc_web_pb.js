/**
 * @fileoverview gRPC-Web generated client stub for nexus.meta_api.proto
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');


var nexus_models_proto_typed_document_pb = require('../../../nexus/models/proto/typed_document_pb.js')
const proto = {};
proto.nexus = {};
proto.nexus.meta_api = {};
proto.nexus.meta_api.proto = require('./search_service_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.nexus.meta_api.proto.SearchClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'binary';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.nexus.meta_api.proto.SearchPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options['format'] = 'binary';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.nexus.meta_api.proto.SearchRequest,
 *   !proto.nexus.meta_api.proto.SearchResponse>}
 */
const methodDescriptor_Search_search = new grpc.web.MethodDescriptor(
  '/nexus.meta_api.proto.Search/search',
  grpc.web.MethodType.UNARY,
  proto.nexus.meta_api.proto.SearchRequest,
  proto.nexus.meta_api.proto.SearchResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.SearchRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.SearchResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.nexus.meta_api.proto.SearchRequest,
 *   !proto.nexus.meta_api.proto.SearchResponse>}
 */
const methodInfo_Search_search = new grpc.web.AbstractClientBase.MethodInfo(
  proto.nexus.meta_api.proto.SearchResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.SearchRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.SearchResponse.deserializeBinary
);


/**
 * @param {!proto.nexus.meta_api.proto.SearchRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.nexus.meta_api.proto.SearchResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.nexus.meta_api.proto.SearchResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.nexus.meta_api.proto.SearchClient.prototype.search =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/nexus.meta_api.proto.Search/search',
      request,
      metadata || {},
      methodDescriptor_Search_search,
      callback);
};


/**
 * @param {!proto.nexus.meta_api.proto.SearchRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.nexus.meta_api.proto.SearchResponse>}
 *     Promise that resolves to the response
 */
proto.nexus.meta_api.proto.SearchPromiseClient.prototype.search =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/nexus.meta_api.proto.Search/search',
      request,
      metadata || {},
      methodDescriptor_Search_search);
};


module.exports = proto.nexus.meta_api.proto;

