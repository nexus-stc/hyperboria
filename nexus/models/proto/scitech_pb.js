// source: nexus/models/proto/scitech.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.nexus.models.proto.Scitech', null, global);
goog.exportSymbol('proto.nexus.models.proto.Scitech.OptionalIssuedAtCase', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.nexus.models.proto.Scitech = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.nexus.models.proto.Scitech.repeatedFields_, proto.nexus.models.proto.Scitech.oneofGroups_);
};
goog.inherits(proto.nexus.models.proto.Scitech, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.nexus.models.proto.Scitech.displayName = 'proto.nexus.models.proto.Scitech';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.nexus.models.proto.Scitech.repeatedFields_ = [2,30,12,19];

/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.nexus.models.proto.Scitech.oneofGroups_ = [[25]];

/**
 * @enum {number}
 */
proto.nexus.models.proto.Scitech.OptionalIssuedAtCase = {
  OPTIONAL_ISSUED_AT_NOT_SET: 0,
  ISSUED_AT: 25
};

/**
 * @return {proto.nexus.models.proto.Scitech.OptionalIssuedAtCase}
 */
proto.nexus.models.proto.Scitech.prototype.getOptionalIssuedAtCase = function() {
  return /** @type {proto.nexus.models.proto.Scitech.OptionalIssuedAtCase} */(jspb.Message.computeOneofCase(this, proto.nexus.models.proto.Scitech.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.nexus.models.proto.Scitech.prototype.toObject = function(opt_includeInstance) {
  return proto.nexus.models.proto.Scitech.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.nexus.models.proto.Scitech} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.nexus.models.proto.Scitech.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, 0),
    authorsList: (f = jspb.Message.getRepeatedField(msg, 2)) == null ? undefined : f,
    cu: jspb.Message.getFieldWithDefault(msg, 3, ""),
    cuSuf: jspb.Message.getFieldWithDefault(msg, 4, ""),
    description: jspb.Message.getFieldWithDefault(msg, 5, ""),
    doi: jspb.Message.getFieldWithDefault(msg, 6, ""),
    downloadsCount: jspb.Message.getFieldWithDefault(msg, 28, 0),
    edition: jspb.Message.getFieldWithDefault(msg, 7, ""),
    extension: jspb.Message.getFieldWithDefault(msg, 8, ""),
    fictionId: jspb.Message.getFieldWithDefault(msg, 9, 0),
    filesize: jspb.Message.getFieldWithDefault(msg, 10, 0),
    ipfsMultihashesList: (f = jspb.Message.getRepeatedField(msg, 30)) == null ? undefined : f,
    isDeleted: jspb.Message.getBooleanFieldWithDefault(msg, 11, false),
    isbnsList: (f = jspb.Message.getRepeatedField(msg, 12)) == null ? undefined : f,
    hasDuplicates: jspb.Message.getBooleanFieldWithDefault(msg, 31, false),
    issuedAt: jspb.Message.getFieldWithDefault(msg, 25, 0),
    language: jspb.Message.getFieldWithDefault(msg, 13, ""),
    libgenId: jspb.Message.getFieldWithDefault(msg, 14, 0),
    metaLanguage: jspb.Message.getFieldWithDefault(msg, 15, ""),
    md5: jspb.Message.getFieldWithDefault(msg, 16, ""),
    originalId: jspb.Message.getFieldWithDefault(msg, 23, 0),
    pages: jspb.Message.getFieldWithDefault(msg, 17, 0),
    series: jspb.Message.getFieldWithDefault(msg, 18, ""),
    tagsList: (f = jspb.Message.getRepeatedField(msg, 19)) == null ? undefined : f,
    telegramFileId: jspb.Message.getFieldWithDefault(msg, 20, ""),
    title: jspb.Message.getFieldWithDefault(msg, 21, ""),
    updatedAt: jspb.Message.getFieldWithDefault(msg, 22, 0),
    volume: jspb.Message.getFieldWithDefault(msg, 24, ""),
    year: jspb.Message.getFieldWithDefault(msg, 29, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.nexus.models.proto.Scitech}
 */
proto.nexus.models.proto.Scitech.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.nexus.models.proto.Scitech;
  return proto.nexus.models.proto.Scitech.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.nexus.models.proto.Scitech} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.nexus.models.proto.Scitech}
 */
proto.nexus.models.proto.Scitech.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setId(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.addAuthors(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setCu(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setCuSuf(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setDescription(value);
      break;
    case 6:
      var value = /** @type {string} */ (reader.readString());
      msg.setDoi(value);
      break;
    case 28:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setDownloadsCount(value);
      break;
    case 7:
      var value = /** @type {string} */ (reader.readString());
      msg.setEdition(value);
      break;
    case 8:
      var value = /** @type {string} */ (reader.readString());
      msg.setExtension$(value);
      break;
    case 9:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setFictionId(value);
      break;
    case 10:
      var value = /** @type {number} */ (reader.readUint64());
      msg.setFilesize(value);
      break;
    case 30:
      var value = /** @type {string} */ (reader.readString());
      msg.addIpfsMultihashes(value);
      break;
    case 11:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsDeleted(value);
      break;
    case 12:
      var value = /** @type {string} */ (reader.readString());
      msg.addIsbns(value);
      break;
    case 31:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasDuplicates(value);
      break;
    case 25:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setIssuedAt(value);
      break;
    case 13:
      var value = /** @type {string} */ (reader.readString());
      msg.setLanguage(value);
      break;
    case 14:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setLibgenId(value);
      break;
    case 15:
      var value = /** @type {string} */ (reader.readString());
      msg.setMetaLanguage(value);
      break;
    case 16:
      var value = /** @type {string} */ (reader.readString());
      msg.setMd5(value);
      break;
    case 23:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setOriginalId(value);
      break;
    case 17:
      var value = /** @type {number} */ (reader.readUint32());
      msg.setPages(value);
      break;
    case 18:
      var value = /** @type {string} */ (reader.readString());
      msg.setSeries(value);
      break;
    case 19:
      var value = /** @type {string} */ (reader.readString());
      msg.addTags(value);
      break;
    case 20:
      var value = /** @type {string} */ (reader.readString());
      msg.setTelegramFileId(value);
      break;
    case 21:
      var value = /** @type {string} */ (reader.readString());
      msg.setTitle(value);
      break;
    case 22:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setUpdatedAt(value);
      break;
    case 24:
      var value = /** @type {string} */ (reader.readString());
      msg.setVolume(value);
      break;
    case 29:
      var value = /** @type {string} */ (reader.readString());
      msg.setYear(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.nexus.models.proto.Scitech.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.nexus.models.proto.Scitech.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.nexus.models.proto.Scitech} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.nexus.models.proto.Scitech.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f !== 0) {
    writer.writeInt64(
      1,
      f
    );
  }
  f = message.getAuthorsList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      2,
      f
    );
  }
  f = message.getCu();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getCuSuf();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getDescription();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
  f = message.getDoi();
  if (f.length > 0) {
    writer.writeString(
      6,
      f
    );
  }
  f = message.getDownloadsCount();
  if (f !== 0) {
    writer.writeUint32(
      28,
      f
    );
  }
  f = message.getEdition();
  if (f.length > 0) {
    writer.writeString(
      7,
      f
    );
  }
  f = message.getExtension$();
  if (f.length > 0) {
    writer.writeString(
      8,
      f
    );
  }
  f = message.getFictionId();
  if (f !== 0) {
    writer.writeInt64(
      9,
      f
    );
  }
  f = message.getFilesize();
  if (f !== 0) {
    writer.writeUint64(
      10,
      f
    );
  }
  f = message.getIpfsMultihashesList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      30,
      f
    );
  }
  f = message.getIsDeleted();
  if (f) {
    writer.writeBool(
      11,
      f
    );
  }
  f = message.getIsbnsList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      12,
      f
    );
  }
  f = message.getHasDuplicates();
  if (f) {
    writer.writeBool(
      31,
      f
    );
  }
  f = /** @type {number} */ (jspb.Message.getField(message, 25));
  if (f != null) {
    writer.writeInt64(
      25,
      f
    );
  }
  f = message.getLanguage();
  if (f.length > 0) {
    writer.writeString(
      13,
      f
    );
  }
  f = message.getLibgenId();
  if (f !== 0) {
    writer.writeInt64(
      14,
      f
    );
  }
  f = message.getMetaLanguage();
  if (f.length > 0) {
    writer.writeString(
      15,
      f
    );
  }
  f = message.getMd5();
  if (f.length > 0) {
    writer.writeString(
      16,
      f
    );
  }
  f = message.getOriginalId();
  if (f !== 0) {
    writer.writeInt64(
      23,
      f
    );
  }
  f = message.getPages();
  if (f !== 0) {
    writer.writeUint32(
      17,
      f
    );
  }
  f = message.getSeries();
  if (f.length > 0) {
    writer.writeString(
      18,
      f
    );
  }
  f = message.getTagsList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      19,
      f
    );
  }
  f = message.getTelegramFileId();
  if (f.length > 0) {
    writer.writeString(
      20,
      f
    );
  }
  f = message.getTitle();
  if (f.length > 0) {
    writer.writeString(
      21,
      f
    );
  }
  f = message.getUpdatedAt();
  if (f !== 0) {
    writer.writeInt32(
      22,
      f
    );
  }
  f = message.getVolume();
  if (f.length > 0) {
    writer.writeString(
      24,
      f
    );
  }
  f = message.getYear();
  if (f.length > 0) {
    writer.writeString(
      29,
      f
    );
  }
};


/**
 * optional int64 id = 1;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getId = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setId = function(value) {
  return jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * repeated string authors = 2;
 * @return {!Array<string>}
 */
proto.nexus.models.proto.Scitech.prototype.getAuthorsList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 2));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setAuthorsList = function(value) {
  return jspb.Message.setField(this, 2, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.addAuthors = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 2, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.clearAuthorsList = function() {
  return this.setAuthorsList([]);
};


/**
 * optional string cu = 3;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getCu = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setCu = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string cu_suf = 4;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getCuSuf = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setCuSuf = function(value) {
  return jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional string description = 5;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getDescription = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setDescription = function(value) {
  return jspb.Message.setProto3StringField(this, 5, value);
};


/**
 * optional string doi = 6;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getDoi = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 6, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setDoi = function(value) {
  return jspb.Message.setProto3StringField(this, 6, value);
};


/**
 * optional uint32 downloads_count = 28;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getDownloadsCount = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 28, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setDownloadsCount = function(value) {
  return jspb.Message.setProto3IntField(this, 28, value);
};


/**
 * optional string edition = 7;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getEdition = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 7, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setEdition = function(value) {
  return jspb.Message.setProto3StringField(this, 7, value);
};


/**
 * optional string extension = 8;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getExtension$ = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 8, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setExtension$ = function(value) {
  return jspb.Message.setProto3StringField(this, 8, value);
};


/**
 * optional int64 fiction_id = 9;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getFictionId = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 9, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setFictionId = function(value) {
  return jspb.Message.setProto3IntField(this, 9, value);
};


/**
 * optional uint64 filesize = 10;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getFilesize = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 10, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setFilesize = function(value) {
  return jspb.Message.setProto3IntField(this, 10, value);
};


/**
 * repeated string ipfs_multihashes = 30;
 * @return {!Array<string>}
 */
proto.nexus.models.proto.Scitech.prototype.getIpfsMultihashesList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 30));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setIpfsMultihashesList = function(value) {
  return jspb.Message.setField(this, 30, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.addIpfsMultihashes = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 30, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.clearIpfsMultihashesList = function() {
  return this.setIpfsMultihashesList([]);
};


/**
 * optional bool is_deleted = 11;
 * @return {boolean}
 */
proto.nexus.models.proto.Scitech.prototype.getIsDeleted = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 11, false));
};


/**
 * @param {boolean} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setIsDeleted = function(value) {
  return jspb.Message.setProto3BooleanField(this, 11, value);
};


/**
 * repeated string isbns = 12;
 * @return {!Array<string>}
 */
proto.nexus.models.proto.Scitech.prototype.getIsbnsList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 12));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setIsbnsList = function(value) {
  return jspb.Message.setField(this, 12, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.addIsbns = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 12, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.clearIsbnsList = function() {
  return this.setIsbnsList([]);
};


/**
 * optional bool has_duplicates = 31;
 * @return {boolean}
 */
proto.nexus.models.proto.Scitech.prototype.getHasDuplicates = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 31, false));
};


/**
 * @param {boolean} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setHasDuplicates = function(value) {
  return jspb.Message.setProto3BooleanField(this, 31, value);
};


/**
 * optional int64 issued_at = 25;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getIssuedAt = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 25, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setIssuedAt = function(value) {
  return jspb.Message.setOneofField(this, 25, proto.nexus.models.proto.Scitech.oneofGroups_[0], value);
};


/**
 * Clears the field making it undefined.
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.clearIssuedAt = function() {
  return jspb.Message.setOneofField(this, 25, proto.nexus.models.proto.Scitech.oneofGroups_[0], undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.nexus.models.proto.Scitech.prototype.hasIssuedAt = function() {
  return jspb.Message.getField(this, 25) != null;
};


/**
 * optional string language = 13;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getLanguage = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 13, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setLanguage = function(value) {
  return jspb.Message.setProto3StringField(this, 13, value);
};


/**
 * optional int64 libgen_id = 14;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getLibgenId = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 14, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setLibgenId = function(value) {
  return jspb.Message.setProto3IntField(this, 14, value);
};


/**
 * optional string meta_language = 15;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getMetaLanguage = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 15, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setMetaLanguage = function(value) {
  return jspb.Message.setProto3StringField(this, 15, value);
};


/**
 * optional string md5 = 16;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getMd5 = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 16, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setMd5 = function(value) {
  return jspb.Message.setProto3StringField(this, 16, value);
};


/**
 * optional int64 original_id = 23;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getOriginalId = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 23, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setOriginalId = function(value) {
  return jspb.Message.setProto3IntField(this, 23, value);
};


/**
 * optional uint32 pages = 17;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getPages = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 17, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setPages = function(value) {
  return jspb.Message.setProto3IntField(this, 17, value);
};


/**
 * optional string series = 18;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getSeries = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 18, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setSeries = function(value) {
  return jspb.Message.setProto3StringField(this, 18, value);
};


/**
 * repeated string tags = 19;
 * @return {!Array<string>}
 */
proto.nexus.models.proto.Scitech.prototype.getTagsList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 19));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setTagsList = function(value) {
  return jspb.Message.setField(this, 19, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.addTags = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 19, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.clearTagsList = function() {
  return this.setTagsList([]);
};


/**
 * optional string telegram_file_id = 20;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getTelegramFileId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 20, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setTelegramFileId = function(value) {
  return jspb.Message.setProto3StringField(this, 20, value);
};


/**
 * optional string title = 21;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getTitle = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 21, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setTitle = function(value) {
  return jspb.Message.setProto3StringField(this, 21, value);
};


/**
 * optional int32 updated_at = 22;
 * @return {number}
 */
proto.nexus.models.proto.Scitech.prototype.getUpdatedAt = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 22, 0));
};


/**
 * @param {number} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setUpdatedAt = function(value) {
  return jspb.Message.setProto3IntField(this, 22, value);
};


/**
 * optional string volume = 24;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getVolume = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 24, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setVolume = function(value) {
  return jspb.Message.setProto3StringField(this, 24, value);
};


/**
 * optional string year = 29;
 * @return {string}
 */
proto.nexus.models.proto.Scitech.prototype.getYear = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 29, ""));
};


/**
 * @param {string} value
 * @return {!proto.nexus.models.proto.Scitech} returns this
 */
proto.nexus.models.proto.Scitech.prototype.setYear = function(value) {
  return jspb.Message.setProto3StringField(this, 29, value);
};


goog.object.extend(exports, proto.nexus.models.proto);
