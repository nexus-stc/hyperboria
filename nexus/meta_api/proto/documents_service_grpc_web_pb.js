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
proto.nexus.meta_api.proto = require('./documents_service_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?Object} options
 * @constructor
 * @struct
 * @final
 */
proto.nexus.meta_api.proto.DocumentsClient =
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
proto.nexus.meta_api.proto.DocumentsPromiseClient =
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
 *   !proto.nexus.meta_api.proto.TypedDocumentRequest,
 *   !proto.nexus.models.proto.TypedDocument>}
 */
const methodDescriptor_Documents_get = new grpc.web.MethodDescriptor(
  '/nexus.meta_api.proto.Documents/get',
  grpc.web.MethodType.UNARY,
  proto.nexus.meta_api.proto.TypedDocumentRequest,
  nexus_models_proto_typed_document_pb.TypedDocument,
  /**
   * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  nexus_models_proto_typed_document_pb.TypedDocument.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.nexus.meta_api.proto.TypedDocumentRequest,
 *   !proto.nexus.models.proto.TypedDocument>}
 */
const methodInfo_Documents_get = new grpc.web.AbstractClientBase.MethodInfo(
  nexus_models_proto_typed_document_pb.TypedDocument,
  /**
   * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  nexus_models_proto_typed_document_pb.TypedDocument.deserializeBinary
);


/**
 * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.nexus.models.proto.TypedDocument)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.nexus.models.proto.TypedDocument>|undefined}
 *     The XHR Node Readable Stream
 */
proto.nexus.meta_api.proto.DocumentsClient.prototype.get =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/get',
      request,
      metadata || {},
      methodDescriptor_Documents_get,
      callback);
};


/**
 * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.nexus.models.proto.TypedDocument>}
 *     Promise that resolves to the response
 */
proto.nexus.meta_api.proto.DocumentsPromiseClient.prototype.get =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/get',
      request,
      metadata || {},
      methodDescriptor_Documents_get);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.nexus.meta_api.proto.TypedDocumentRequest,
 *   !proto.nexus.meta_api.proto.GetViewResponse>}
 */
const methodDescriptor_Documents_get_view = new grpc.web.MethodDescriptor(
  '/nexus.meta_api.proto.Documents/get_view',
  grpc.web.MethodType.UNARY,
  proto.nexus.meta_api.proto.TypedDocumentRequest,
  proto.nexus.meta_api.proto.GetViewResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.GetViewResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.nexus.meta_api.proto.TypedDocumentRequest,
 *   !proto.nexus.meta_api.proto.GetViewResponse>}
 */
const methodInfo_Documents_get_view = new grpc.web.AbstractClientBase.MethodInfo(
  proto.nexus.meta_api.proto.GetViewResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.GetViewResponse.deserializeBinary
);


/**
 * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.nexus.meta_api.proto.GetViewResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.nexus.meta_api.proto.GetViewResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.nexus.meta_api.proto.DocumentsClient.prototype.get_view =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/get_view',
      request,
      metadata || {},
      methodDescriptor_Documents_get_view,
      callback);
};


/**
 * @param {!proto.nexus.meta_api.proto.TypedDocumentRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.nexus.meta_api.proto.GetViewResponse>}
 *     Promise that resolves to the response
 */
proto.nexus.meta_api.proto.DocumentsPromiseClient.prototype.get_view =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/get_view',
      request,
      metadata || {},
      methodDescriptor_Documents_get_view);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.nexus.meta_api.proto.RollRequest,
 *   !proto.nexus.meta_api.proto.RollResponse>}
 */
const methodDescriptor_Documents_roll = new grpc.web.MethodDescriptor(
  '/nexus.meta_api.proto.Documents/roll',
  grpc.web.MethodType.UNARY,
  proto.nexus.meta_api.proto.RollRequest,
  proto.nexus.meta_api.proto.RollResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.RollRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.RollResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.nexus.meta_api.proto.RollRequest,
 *   !proto.nexus.meta_api.proto.RollResponse>}
 */
const methodInfo_Documents_roll = new grpc.web.AbstractClientBase.MethodInfo(
  proto.nexus.meta_api.proto.RollResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.RollRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.RollResponse.deserializeBinary
);


/**
 * @param {!proto.nexus.meta_api.proto.RollRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.nexus.meta_api.proto.RollResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.nexus.meta_api.proto.RollResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.nexus.meta_api.proto.DocumentsClient.prototype.roll =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/roll',
      request,
      metadata || {},
      methodDescriptor_Documents_roll,
      callback);
};


/**
 * @param {!proto.nexus.meta_api.proto.RollRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.nexus.meta_api.proto.RollResponse>}
 *     Promise that resolves to the response
 */
proto.nexus.meta_api.proto.DocumentsPromiseClient.prototype.roll =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/roll',
      request,
      metadata || {},
      methodDescriptor_Documents_roll);
};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.nexus.meta_api.proto.TopMissedRequest,
 *   !proto.nexus.meta_api.proto.TopMissedResponse>}
 */
const methodDescriptor_Documents_top_missed = new grpc.web.MethodDescriptor(
  '/nexus.meta_api.proto.Documents/top_missed',
  grpc.web.MethodType.UNARY,
  proto.nexus.meta_api.proto.TopMissedRequest,
  proto.nexus.meta_api.proto.TopMissedResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.TopMissedRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.TopMissedResponse.deserializeBinary
);


/**
 * @const
 * @type {!grpc.web.AbstractClientBase.MethodInfo<
 *   !proto.nexus.meta_api.proto.TopMissedRequest,
 *   !proto.nexus.meta_api.proto.TopMissedResponse>}
 */
const methodInfo_Documents_top_missed = new grpc.web.AbstractClientBase.MethodInfo(
  proto.nexus.meta_api.proto.TopMissedResponse,
  /**
   * @param {!proto.nexus.meta_api.proto.TopMissedRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.nexus.meta_api.proto.TopMissedResponse.deserializeBinary
);


/**
 * @param {!proto.nexus.meta_api.proto.TopMissedRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.Error, ?proto.nexus.meta_api.proto.TopMissedResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.nexus.meta_api.proto.TopMissedResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.nexus.meta_api.proto.DocumentsClient.prototype.top_missed =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/top_missed',
      request,
      metadata || {},
      methodDescriptor_Documents_top_missed,
      callback);
};


/**
 * @param {!proto.nexus.meta_api.proto.TopMissedRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.nexus.meta_api.proto.TopMissedResponse>}
 *     Promise that resolves to the response
 */
proto.nexus.meta_api.proto.DocumentsPromiseClient.prototype.top_missed =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/nexus.meta_api.proto.Documents/top_missed',
      request,
      metadata || {},
      methodDescriptor_Documents_top_missed);
};


module.exports = proto.nexus.meta_api.proto;

