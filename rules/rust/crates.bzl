"""
@generated
cargo-raze generated Bazel file.

DO NOT EDIT! Replaced on runs of cargo-raze
"""

load("@bazel_tools//tools/build_defs/repo:git.bzl", "new_git_repository")  # buildifier: disable=load
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")  # buildifier: disable=load
load("@bazel_tools//tools/build_defs/repo:utils.bzl", "maybe")  # buildifier: disable=load

def raze_fetch_remote_crates():
    """This function defines a collection of repos and should be called in a WORKSPACE file"""
    maybe(
        http_archive,
        name = "raze__ahash__0_4_7",
        url = "https://crates.io/api/v1/crates/ahash/0.4.7/download",
        type = "tar.gz",
        sha256 = "739f4a8db6605981345c5654f3a85b056ce52f37a39d34da03f25bf2151ea16e",
        strip_prefix = "ahash-0.4.7",
        build_file = Label("//rules/rust/remote:BUILD.ahash-0.4.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ahash__0_7_6",
        url = "https://crates.io/api/v1/crates/ahash/0.7.6/download",
        type = "tar.gz",
        sha256 = "fcb51a0695d8f838b1ee009b3fbf66bda078cd64590202a864a8f3e8c4315c47",
        strip_prefix = "ahash-0.7.6",
        build_file = Label("//rules/rust/remote:BUILD.ahash-0.7.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__aho_corasick__0_7_18",
        url = "https://crates.io/api/v1/crates/aho-corasick/0.7.18/download",
        type = "tar.gz",
        sha256 = "1e37cfd5e7657ada45f742d6e99ca5788580b5c529dc78faf11ece6dc702656f",
        strip_prefix = "aho-corasick-0.7.18",
        build_file = Label("//rules/rust/remote:BUILD.aho-corasick-0.7.18.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__alloc_no_stdlib__2_0_3",
        url = "https://crates.io/api/v1/crates/alloc-no-stdlib/2.0.3/download",
        type = "tar.gz",
        sha256 = "35ef4730490ad1c4eae5c4325b2a95f521d023e5c885853ff7aca0a6a1631db3",
        strip_prefix = "alloc-no-stdlib-2.0.3",
        build_file = Label("//rules/rust/remote:BUILD.alloc-no-stdlib-2.0.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__alloc_stdlib__0_2_1",
        url = "https://crates.io/api/v1/crates/alloc-stdlib/0.2.1/download",
        type = "tar.gz",
        sha256 = "697ed7edc0f1711de49ce108c541623a0af97c6c60b2f6e2b65229847ac843c2",
        strip_prefix = "alloc-stdlib-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.alloc-stdlib-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ansi_term__0_12_1",
        url = "https://crates.io/api/v1/crates/ansi_term/0.12.1/download",
        type = "tar.gz",
        sha256 = "d52a9bb7ec0cf484c551830a7ce27bd20d67eac647e1befb56b0be4ee39a55d2",
        strip_prefix = "ansi_term-0.12.1",
        build_file = Label("//rules/rust/remote:BUILD.ansi_term-0.12.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__anyhow__1_0_56",
        url = "https://crates.io/api/v1/crates/anyhow/1.0.56/download",
        type = "tar.gz",
        sha256 = "4361135be9122e0870de935d7c439aef945b9f9ddd4199a553b5270b49c82a27",
        strip_prefix = "anyhow-1.0.56",
        build_file = Label("//rules/rust/remote:BUILD.anyhow-1.0.56.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__async_stream__0_3_3",
        url = "https://crates.io/api/v1/crates/async-stream/0.3.3/download",
        type = "tar.gz",
        sha256 = "dad5c83079eae9969be7fadefe640a1c566901f05ff91ab221de4b6f68d9507e",
        strip_prefix = "async-stream-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.async-stream-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__async_stream_impl__0_3_3",
        url = "https://crates.io/api/v1/crates/async-stream-impl/0.3.3/download",
        type = "tar.gz",
        sha256 = "10f203db73a71dfa2fb6dd22763990fa26f3d2625a6da2da900d23b87d26be27",
        strip_prefix = "async-stream-impl-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.async-stream-impl-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__async_trait__0_1_52",
        url = "https://crates.io/api/v1/crates/async-trait/0.1.52/download",
        type = "tar.gz",
        sha256 = "061a7acccaa286c011ddc30970520b98fa40e00c9d644633fb26b5fc63a265e3",
        strip_prefix = "async-trait-0.1.52",
        build_file = Label("//rules/rust/remote:BUILD.async-trait-0.1.52.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__atty__0_2_14",
        url = "https://crates.io/api/v1/crates/atty/0.2.14/download",
        type = "tar.gz",
        sha256 = "d9b39be18770d11421cdb1b9947a45dd3f37e93092cbf377614828a319d5fee8",
        strip_prefix = "atty-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.atty-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__autocfg__1_1_0",
        url = "https://crates.io/api/v1/crates/autocfg/1.1.0/download",
        type = "tar.gz",
        sha256 = "d468802bab17cbc0cc575e9b053f41e72aa36bfa6b7f55e3529ffa43161b97fa",
        strip_prefix = "autocfg-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.autocfg-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__base64__0_13_0",
        url = "https://crates.io/api/v1/crates/base64/0.13.0/download",
        type = "tar.gz",
        sha256 = "904dfeac50f3cdaba28fc6f57fdcddb75f49ed61346676a78c4ffe55877802fd",
        strip_prefix = "base64-0.13.0",
        build_file = Label("//rules/rust/remote:BUILD.base64-0.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bitflags__1_3_2",
        url = "https://crates.io/api/v1/crates/bitflags/1.3.2/download",
        type = "tar.gz",
        sha256 = "bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a",
        strip_prefix = "bitflags-1.3.2",
        build_file = Label("//rules/rust/remote:BUILD.bitflags-1.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bitpacking__0_8_4",
        url = "https://crates.io/api/v1/crates/bitpacking/0.8.4/download",
        type = "tar.gz",
        sha256 = "a8c7d2ac73c167c06af4a5f37e6e59d84148d57ccbe4480b76f0273eefea82d7",
        strip_prefix = "bitpacking-0.8.4",
        build_file = Label("//rules/rust/remote:BUILD.bitpacking-0.8.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__block_buffer__0_7_3",
        url = "https://crates.io/api/v1/crates/block-buffer/0.7.3/download",
        type = "tar.gz",
        sha256 = "c0940dc441f31689269e10ac70eb1002a3a1d3ad1390e030043662eb7fe4688b",
        strip_prefix = "block-buffer-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.block-buffer-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__block_padding__0_1_5",
        url = "https://crates.io/api/v1/crates/block-padding/0.1.5/download",
        type = "tar.gz",
        sha256 = "fa79dedbb091f449f1f39e53edf88d5dbe95f895dae6135a8d7b881fb5af73f5",
        strip_prefix = "block-padding-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.block-padding-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__brotli__3_3_3",
        url = "https://crates.io/api/v1/crates/brotli/3.3.3/download",
        type = "tar.gz",
        sha256 = "f838e47a451d5a8fa552371f80024dd6ace9b7acdf25c4c3d0f9bc6816fb1c39",
        strip_prefix = "brotli-3.3.3",
        build_file = Label("//rules/rust/remote:BUILD.brotli-3.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__brotli_decompressor__2_3_2",
        url = "https://crates.io/api/v1/crates/brotli-decompressor/2.3.2/download",
        type = "tar.gz",
        sha256 = "59ad2d4653bf5ca36ae797b1f4bb4dbddb60ce49ca4aed8a2ce4829f60425b80",
        strip_prefix = "brotli-decompressor-2.3.2",
        build_file = Label("//rules/rust/remote:BUILD.brotli-decompressor-2.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bumpalo__3_9_1",
        url = "https://crates.io/api/v1/crates/bumpalo/3.9.1/download",
        type = "tar.gz",
        sha256 = "a4a45a46ab1f2412e53d3a0ade76ffad2025804294569aae387231a0cd6e0899",
        strip_prefix = "bumpalo-3.9.1",
        build_file = Label("//rules/rust/remote:BUILD.bumpalo-3.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__byte_tools__0_3_1",
        url = "https://crates.io/api/v1/crates/byte-tools/0.3.1/download",
        type = "tar.gz",
        sha256 = "e3b5ca7a04898ad4bcd41c90c5285445ff5b791899bb1b0abdd2a2aa791211d7",
        strip_prefix = "byte-tools-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.byte-tools-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__byteorder__1_4_3",
        url = "https://crates.io/api/v1/crates/byteorder/1.4.3/download",
        type = "tar.gz",
        sha256 = "14c189c53d098945499cdfa7ecc63567cf3886b3332b312a5b4585d8d3a6a610",
        strip_prefix = "byteorder-1.4.3",
        build_file = Label("//rules/rust/remote:BUILD.byteorder-1.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__bytes__1_1_0",
        url = "https://crates.io/api/v1/crates/bytes/1.1.0/download",
        type = "tar.gz",
        sha256 = "c4872d67bab6358e59559027aa3b9157c53d9358c51423c17554809a8858e0f8",
        strip_prefix = "bytes-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.bytes-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cc__1_0_73",
        url = "https://crates.io/api/v1/crates/cc/1.0.73/download",
        type = "tar.gz",
        sha256 = "2fff2a6927b3bb87f9595d67196a70493f627687a71d87a0d692242c33f58c11",
        strip_prefix = "cc-1.0.73",
        build_file = Label("//rules/rust/remote:BUILD.cc-1.0.73.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__census__0_4_0",
        url = "https://crates.io/api/v1/crates/census/0.4.0/download",
        type = "tar.gz",
        sha256 = "5927edd8345aef08578bcbb4aea7314f340d80c7f4931f99fbeb40b99d8f5060",
        strip_prefix = "census-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.census-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__cfg_if__1_0_0",
        url = "https://crates.io/api/v1/crates/cfg-if/1.0.0/download",
        type = "tar.gz",
        sha256 = "baf1de4339761588bc0619e3cbc0120ee582ebb74b53b4efbf79117bd2da40fd",
        strip_prefix = "cfg-if-1.0.0",
        build_file = Label("//rules/rust/remote:BUILD.cfg-if-1.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__chrono__0_4_19",
        url = "https://crates.io/api/v1/crates/chrono/0.4.19/download",
        type = "tar.gz",
        sha256 = "670ad68c9088c2a963aaa298cb369688cf3f9465ce5e2d4ca10e6e0098a1ce73",
        strip_prefix = "chrono-0.4.19",
        build_file = Label("//rules/rust/remote:BUILD.chrono-0.4.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__clap__3_1_6",
        url = "https://crates.io/api/v1/crates/clap/3.1.6/download",
        type = "tar.gz",
        sha256 = "d8c93436c21e4698bacadf42917db28b23017027a4deccb35dbe47a7e7840123",
        strip_prefix = "clap-3.1.6",
        build_file = Label("//rules/rust/remote:BUILD.clap-3.1.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__colored__2_0_0",
        url = "https://crates.io/api/v1/crates/colored/2.0.0/download",
        type = "tar.gz",
        sha256 = "b3616f750b84d8f0de8a58bda93e08e2a81ad3f523089b05f1dffecab48c6cbd",
        strip_prefix = "colored-2.0.0",
        build_file = Label("//rules/rust/remote:BUILD.colored-2.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__combine__4_6_3",
        url = "https://crates.io/api/v1/crates/combine/4.6.3/download",
        type = "tar.gz",
        sha256 = "50b727aacc797f9fc28e355d21f34709ac4fc9adecfe470ad07b8f4464f53062",
        strip_prefix = "combine-4.6.3",
        build_file = Label("//rules/rust/remote:BUILD.combine-4.6.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__config__0_12_0",
        url = "https://crates.io/api/v1/crates/config/0.12.0/download",
        type = "tar.gz",
        sha256 = "54ad70579325f1a38ea4c13412b82241c5900700a69785d73e2736bd65a33f86",
        strip_prefix = "config-0.12.0",
        build_file = Label("//rules/rust/remote:BUILD.config-0.12.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crc32fast__1_3_2",
        url = "https://crates.io/api/v1/crates/crc32fast/1.3.2/download",
        type = "tar.gz",
        sha256 = "b540bd8bc810d3885c6ea91e2018302f68baba2129ab3e88f32389ee9370880d",
        strip_prefix = "crc32fast-1.3.2",
        build_file = Label("//rules/rust/remote:BUILD.crc32fast-1.3.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam__0_8_1",
        url = "https://crates.io/api/v1/crates/crossbeam/0.8.1/download",
        type = "tar.gz",
        sha256 = "4ae5588f6b3c3cb05239e90bd110f257254aecd01e4635400391aeae07497845",
        strip_prefix = "crossbeam-0.8.1",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-0.8.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_channel__0_5_4",
        url = "https://crates.io/api/v1/crates/crossbeam-channel/0.5.4/download",
        type = "tar.gz",
        sha256 = "5aaa7bd5fb665c6864b5f963dd9097905c54125909c7aa94c9e18507cdbe6c53",
        strip_prefix = "crossbeam-channel-0.5.4",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-channel-0.5.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_deque__0_8_1",
        url = "https://crates.io/api/v1/crates/crossbeam-deque/0.8.1/download",
        type = "tar.gz",
        sha256 = "6455c0ca19f0d2fbf751b908d5c55c1f5cbc65e03c4225427254b46890bdde1e",
        strip_prefix = "crossbeam-deque-0.8.1",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-deque-0.8.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_epoch__0_9_8",
        url = "https://crates.io/api/v1/crates/crossbeam-epoch/0.9.8/download",
        type = "tar.gz",
        sha256 = "1145cf131a2c6ba0615079ab6a638f7e1973ac9c2634fcbeaaad6114246efe8c",
        strip_prefix = "crossbeam-epoch-0.9.8",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-epoch-0.9.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_queue__0_3_5",
        url = "https://crates.io/api/v1/crates/crossbeam-queue/0.3.5/download",
        type = "tar.gz",
        sha256 = "1f25d8400f4a7a5778f0e4e52384a48cbd9b5c495d110786187fc750075277a2",
        strip_prefix = "crossbeam-queue-0.3.5",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-queue-0.3.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crossbeam_utils__0_8_8",
        url = "https://crates.io/api/v1/crates/crossbeam-utils/0.8.8/download",
        type = "tar.gz",
        sha256 = "0bf124c720b7686e3c2663cf54062ab0f68a88af2fb6a030e87e30bf721fcb38",
        strip_prefix = "crossbeam-utils-0.8.8",
        build_file = Label("//rules/rust/remote:BUILD.crossbeam-utils-0.8.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__crunchy__0_2_2",
        url = "https://crates.io/api/v1/crates/crunchy/0.2.2/download",
        type = "tar.gz",
        sha256 = "7a81dae078cea95a014a339291cec439d2f232ebe854a9d672b796c6afafa9b7",
        strip_prefix = "crunchy-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.crunchy-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ctor__0_1_22",
        url = "https://crates.io/api/v1/crates/ctor/0.1.22/download",
        type = "tar.gz",
        sha256 = "f877be4f7c9f246b183111634f75baa039715e3f46ce860677d3b19a69fb229c",
        strip_prefix = "ctor-0.1.22",
        build_file = Label("//rules/rust/remote:BUILD.ctor-0.1.22.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dashmap__4_0_2",
        url = "https://crates.io/api/v1/crates/dashmap/4.0.2/download",
        type = "tar.gz",
        sha256 = "e77a43b28d0668df09411cb0bc9a8c2adc40f9a048afe863e05fd43251e8e39c",
        strip_prefix = "dashmap-4.0.2",
        build_file = Label("//rules/rust/remote:BUILD.dashmap-4.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__diff__0_1_12",
        url = "https://crates.io/api/v1/crates/diff/0.1.12/download",
        type = "tar.gz",
        sha256 = "0e25ea47919b1560c4e3b7fe0aaab9becf5b84a10325ddf7db0f0ba5e1026499",
        strip_prefix = "diff-0.1.12",
        build_file = Label("//rules/rust/remote:BUILD.diff-0.1.12.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__digest__0_8_1",
        url = "https://crates.io/api/v1/crates/digest/0.8.1/download",
        type = "tar.gz",
        sha256 = "f3d0c8c8752312f9713efd397ff63acb9f85585afbf179282e720e7704954dd5",
        strip_prefix = "digest-0.8.1",
        build_file = Label("//rules/rust/remote:BUILD.digest-0.8.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__dlv_list__0_2_3",
        url = "https://crates.io/api/v1/crates/dlv-list/0.2.3/download",
        type = "tar.gz",
        sha256 = "68df3f2b690c1b86e65ef7830956aededf3cb0a16f898f79b9a6f421a7b6211b",
        strip_prefix = "dlv-list-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.dlv-list-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__downcast_rs__1_2_0",
        url = "https://crates.io/api/v1/crates/downcast-rs/1.2.0/download",
        type = "tar.gz",
        sha256 = "9ea835d29036a4087793836fa931b08837ad5e957da9e23886b29586fb9b6650",
        strip_prefix = "downcast-rs-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.downcast-rs-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__either__1_6_1",
        url = "https://crates.io/api/v1/crates/either/1.6.1/download",
        type = "tar.gz",
        sha256 = "e78d4f1cc4ae33bbfc157ed5d5a5ef3bc29227303d595861deb238fcec4e9457",
        strip_prefix = "either-1.6.1",
        build_file = Label("//rules/rust/remote:BUILD.either-1.6.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fail__0_5_0",
        url = "https://crates.io/api/v1/crates/fail/0.5.0/download",
        type = "tar.gz",
        sha256 = "ec3245a0ca564e7f3c797d20d833a6870f57a728ac967d5225b3ffdef4465011",
        strip_prefix = "fail-0.5.0",
        build_file = Label("//rules/rust/remote:BUILD.fail-0.5.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fake_simd__0_1_2",
        url = "https://crates.io/api/v1/crates/fake-simd/0.1.2/download",
        type = "tar.gz",
        sha256 = "e88a8acf291dafb59c2d96e8f59828f3838bb1a70398823ade51a84de6a6deed",
        strip_prefix = "fake-simd-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.fake-simd-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fastdivide__0_4_0",
        url = "https://crates.io/api/v1/crates/fastdivide/0.4.0/download",
        type = "tar.gz",
        sha256 = "25c7df09945d65ea8d70b3321547ed414bbc540aad5bac6883d021b970f35b04",
        strip_prefix = "fastdivide-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.fastdivide-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fastfield_codecs__0_1_0",
        url = "https://crates.io/api/v1/crates/fastfield_codecs/0.1.0/download",
        type = "tar.gz",
        sha256 = "bb0e8bfa31546b4ace05092c9db8d251d7bbc298a384875a08c945a473de4f1f",
        strip_prefix = "fastfield_codecs-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.fastfield_codecs-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fastrand__1_7_0",
        url = "https://crates.io/api/v1/crates/fastrand/1.7.0/download",
        type = "tar.gz",
        sha256 = "c3fcf0cee53519c866c09b5de1f6c56ff9d647101f81c1964fa632e148896cdf",
        strip_prefix = "fastrand-1.7.0",
        build_file = Label("//rules/rust/remote:BUILD.fastrand-1.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fixedbitset__0_4_1",
        url = "https://crates.io/api/v1/crates/fixedbitset/0.4.1/download",
        type = "tar.gz",
        sha256 = "279fb028e20b3c4c320317955b77c5e0c9701f05a1d309905d6fc702cdc5053e",
        strip_prefix = "fixedbitset-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.fixedbitset-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fnv__1_0_7",
        url = "https://crates.io/api/v1/crates/fnv/1.0.7/download",
        type = "tar.gz",
        sha256 = "3f9eec918d3f24069decb9af1554cad7c880e2da24a9afd88aca000531ab82c1",
        strip_prefix = "fnv-1.0.7",
        build_file = Label("//rules/rust/remote:BUILD.fnv-1.0.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__fs2__0_4_3",
        url = "https://crates.io/api/v1/crates/fs2/0.4.3/download",
        type = "tar.gz",
        sha256 = "9564fc758e15025b46aa6643b1b77d047d1a56a1aea6e01002ac0c7026876213",
        strip_prefix = "fs2-0.4.3",
        build_file = Label("//rules/rust/remote:BUILD.fs2-0.4.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures__0_3_21",
        url = "https://crates.io/api/v1/crates/futures/0.3.21/download",
        type = "tar.gz",
        sha256 = "f73fe65f54d1e12b726f517d3e2135ca3125a437b6d998caf1962961f7172d9e",
        strip_prefix = "futures-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_channel__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-channel/0.3.21/download",
        type = "tar.gz",
        sha256 = "c3083ce4b914124575708913bca19bfe887522d6e2e6d0952943f5eac4a74010",
        strip_prefix = "futures-channel-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-channel-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_core__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-core/0.3.21/download",
        type = "tar.gz",
        sha256 = "0c09fd04b7e4073ac7156a9539b57a484a8ea920f79c7c675d05d289ab6110d3",
        strip_prefix = "futures-core-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-core-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_executor__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-executor/0.3.21/download",
        type = "tar.gz",
        sha256 = "9420b90cfa29e327d0429f19be13e7ddb68fa1cccb09d65e5706b8c7a749b8a6",
        strip_prefix = "futures-executor-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-executor-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_io__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-io/0.3.21/download",
        type = "tar.gz",
        sha256 = "fc4045962a5a5e935ee2fdedaa4e08284547402885ab326734432bed5d12966b",
        strip_prefix = "futures-io-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-io-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_macro__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-macro/0.3.21/download",
        type = "tar.gz",
        sha256 = "33c1e13800337f4d4d7a316bf45a567dbcb6ffe087f16424852d97e97a91f512",
        strip_prefix = "futures-macro-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-macro-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_sink__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-sink/0.3.21/download",
        type = "tar.gz",
        sha256 = "21163e139fa306126e6eedaf49ecdb4588f939600f0b1e770f4205ee4b7fa868",
        strip_prefix = "futures-sink-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-sink-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_task__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-task/0.3.21/download",
        type = "tar.gz",
        sha256 = "57c66a976bf5909d801bbef33416c41372779507e7a6b3a5e25e4749c58f776a",
        strip_prefix = "futures-task-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-task-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__futures_util__0_3_21",
        url = "https://crates.io/api/v1/crates/futures-util/0.3.21/download",
        type = "tar.gz",
        sha256 = "d8b7abd5d659d9b90c8cba917f6ec750a74e2dc23902ef9cd4cc8c8b22e6036a",
        strip_prefix = "futures-util-0.3.21",
        build_file = Label("//rules/rust/remote:BUILD.futures-util-0.3.21.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__generic_array__0_12_4",
        url = "https://crates.io/api/v1/crates/generic-array/0.12.4/download",
        type = "tar.gz",
        sha256 = "ffdf9f34f1447443d37393cc6c2b8313aebddcd96906caf34e54c68d8e57d7bd",
        strip_prefix = "generic-array-0.12.4",
        build_file = Label("//rules/rust/remote:BUILD.generic-array-0.12.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__getrandom__0_2_5",
        url = "https://crates.io/api/v1/crates/getrandom/0.2.5/download",
        type = "tar.gz",
        sha256 = "d39cd93900197114fa1fcb7ae84ca742095eed9442088988ae74fa744e930e77",
        strip_prefix = "getrandom-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.getrandom-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__h2__0_3_12",
        url = "https://crates.io/api/v1/crates/h2/0.3.12/download",
        type = "tar.gz",
        sha256 = "62eeb471aa3e3c9197aa4bfeabfe02982f6dc96f750486c0bb0009ac58b26d2b",
        strip_prefix = "h2-0.3.12",
        build_file = Label("//rules/rust/remote:BUILD.h2-0.3.12.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hashbrown__0_11_2",
        url = "https://crates.io/api/v1/crates/hashbrown/0.11.2/download",
        type = "tar.gz",
        sha256 = "ab5ef0d4909ef3724cc8cce6ccc8572c5c817592e9285f5464f8e86f8bd3726e",
        strip_prefix = "hashbrown-0.11.2",
        build_file = Label("//rules/rust/remote:BUILD.hashbrown-0.11.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hashbrown__0_9_1",
        url = "https://crates.io/api/v1/crates/hashbrown/0.9.1/download",
        type = "tar.gz",
        sha256 = "d7afe4a420e3fe79967a00898cc1f4db7c8a49a9333a29f8a4bd76a253d5cd04",
        strip_prefix = "hashbrown-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.hashbrown-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__heck__0_3_3",
        url = "https://crates.io/api/v1/crates/heck/0.3.3/download",
        type = "tar.gz",
        sha256 = "6d621efb26863f0e9924c6ac577e8275e5e6b77455db64ffa6c65c904e9e132c",
        strip_prefix = "heck-0.3.3",
        build_file = Label("//rules/rust/remote:BUILD.heck-0.3.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hermit_abi__0_1_19",
        url = "https://crates.io/api/v1/crates/hermit-abi/0.1.19/download",
        type = "tar.gz",
        sha256 = "62b467343b94ba476dcb2500d242dadbb39557df889310ac77c5d99100aaac33",
        strip_prefix = "hermit-abi-0.1.19",
        build_file = Label("//rules/rust/remote:BUILD.hermit-abi-0.1.19.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__htmlescape__0_3_1",
        url = "https://crates.io/api/v1/crates/htmlescape/0.3.1/download",
        type = "tar.gz",
        sha256 = "e9025058dae765dee5070ec375f591e2ba14638c63feff74f13805a72e523163",
        strip_prefix = "htmlescape-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.htmlescape-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__http__0_2_6",
        url = "https://crates.io/api/v1/crates/http/0.2.6/download",
        type = "tar.gz",
        sha256 = "31f4c6746584866f0feabcc69893c5b51beef3831656a968ed7ae254cdc4fd03",
        strip_prefix = "http-0.2.6",
        build_file = Label("//rules/rust/remote:BUILD.http-0.2.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__http_body__0_4_4",
        url = "https://crates.io/api/v1/crates/http-body/0.4.4/download",
        type = "tar.gz",
        sha256 = "1ff4f84919677303da5f147645dbea6b1881f368d03ac84e1dc09031ebd7b2c6",
        strip_prefix = "http-body-0.4.4",
        build_file = Label("//rules/rust/remote:BUILD.http-body-0.4.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__http_range_header__0_3_0",
        url = "https://crates.io/api/v1/crates/http-range-header/0.3.0/download",
        type = "tar.gz",
        sha256 = "0bfe8eed0a9285ef776bb792479ea3834e8b94e13d615c2f66d03dd50a435a29",
        strip_prefix = "http-range-header-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.http-range-header-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__httparse__1_6_0",
        url = "https://crates.io/api/v1/crates/httparse/1.6.0/download",
        type = "tar.gz",
        sha256 = "9100414882e15fb7feccb4897e5f0ff0ff1ca7d1a86a23208ada4d7a18e6c6c4",
        strip_prefix = "httparse-1.6.0",
        build_file = Label("//rules/rust/remote:BUILD.httparse-1.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__httpdate__1_0_2",
        url = "https://crates.io/api/v1/crates/httpdate/1.0.2/download",
        type = "tar.gz",
        sha256 = "c4a1e36c821dbe04574f602848a19f742f4fb3c98d40449f11bcad18d6b17421",
        strip_prefix = "httpdate-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.httpdate-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hyper__0_14_17",
        url = "https://crates.io/api/v1/crates/hyper/0.14.17/download",
        type = "tar.gz",
        sha256 = "043f0e083e9901b6cc658a77d1eb86f4fc650bbb977a4337dd63192826aa85dd",
        strip_prefix = "hyper-0.14.17",
        build_file = Label("//rules/rust/remote:BUILD.hyper-0.14.17.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__hyper_timeout__0_4_1",
        url = "https://crates.io/api/v1/crates/hyper-timeout/0.4.1/download",
        type = "tar.gz",
        sha256 = "bbb958482e8c7be4bc3cf272a766a2b0bf1a6755e7a6ae777f017a31d11b13b1",
        strip_prefix = "hyper-timeout-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.hyper-timeout-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__indexmap__1_8_0",
        url = "https://crates.io/api/v1/crates/indexmap/1.8.0/download",
        type = "tar.gz",
        sha256 = "282a6247722caba404c065016bbfa522806e51714c34f5dfc3e4a3a46fcb4223",
        strip_prefix = "indexmap-1.8.0",
        build_file = Label("//rules/rust/remote:BUILD.indexmap-1.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__instant__0_1_12",
        url = "https://crates.io/api/v1/crates/instant/0.1.12/download",
        type = "tar.gz",
        sha256 = "7a5bbe824c507c5da5956355e86a746d82e0e1464f65d862cc5e71da70e94b2c",
        strip_prefix = "instant-0.1.12",
        build_file = Label("//rules/rust/remote:BUILD.instant-0.1.12.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itertools__0_10_3",
        url = "https://crates.io/api/v1/crates/itertools/0.10.3/download",
        type = "tar.gz",
        sha256 = "a9a9d19fa1e79b6215ff29b9d6880b706147f16e9b1dbb1e4e5947b5b02bc5e3",
        strip_prefix = "itertools-0.10.3",
        build_file = Label("//rules/rust/remote:BUILD.itertools-0.10.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__itoa__1_0_1",
        url = "https://crates.io/api/v1/crates/itoa/1.0.1/download",
        type = "tar.gz",
        sha256 = "1aab8fc367588b89dcee83ab0fd66b72b50b72fa1904d7095045ace2b0c81c35",
        strip_prefix = "itoa-1.0.1",
        build_file = Label("//rules/rust/remote:BUILD.itoa-1.0.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__js_sys__0_3_56",
        url = "https://crates.io/api/v1/crates/js-sys/0.3.56/download",
        type = "tar.gz",
        sha256 = "a38fc24e30fd564ce974c02bf1d337caddff65be6cc4735a1f7eab22a7440f04",
        strip_prefix = "js-sys-0.3.56",
        build_file = Label("//rules/rust/remote:BUILD.js-sys-0.3.56.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__json5__0_4_1",
        url = "https://crates.io/api/v1/crates/json5/0.4.1/download",
        type = "tar.gz",
        sha256 = "96b0db21af676c1ce64250b5f40f3ce2cf27e4e47cb91ed91eb6fe9350b430c1",
        strip_prefix = "json5-0.4.1",
        build_file = Label("//rules/rust/remote:BUILD.json5-0.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lazy_static__1_4_0",
        url = "https://crates.io/api/v1/crates/lazy_static/1.4.0/download",
        type = "tar.gz",
        sha256 = "e2abad23fbc42b3700f2f279844dc832adb2b2eb069b2df918f455c4e18cc646",
        strip_prefix = "lazy_static-1.4.0",
        build_file = Label("//rules/rust/remote:BUILD.lazy_static-1.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__levenshtein_automata__0_2_1",
        url = "https://crates.io/api/v1/crates/levenshtein_automata/0.2.1/download",
        type = "tar.gz",
        sha256 = "0c2cdeb66e45e9f36bfad5bbdb4d2384e70936afbee843c6f6543f0c551ebb25",
        strip_prefix = "levenshtein_automata-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.levenshtein_automata-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__libc__0_2_121",
        url = "https://crates.io/api/v1/crates/libc/0.2.121/download",
        type = "tar.gz",
        sha256 = "efaa7b300f3b5fe8eb6bf21ce3895e1751d9665086af2d64b42f19701015ff4f",
        strip_prefix = "libc-0.2.121",
        build_file = Label("//rules/rust/remote:BUILD.libc-0.2.121.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__libz_sys__1_1_5",
        url = "https://crates.io/api/v1/crates/libz-sys/1.1.5/download",
        type = "tar.gz",
        sha256 = "6f35facd4a5673cb5a48822be2be1d4236c1c99cb4113cab7061ac720d5bf859",
        strip_prefix = "libz-sys-1.1.5",
        build_file = Label("//rules/rust/remote:BUILD.libz-sys-1.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__linked_hash_map__0_5_4",
        url = "https://crates.io/api/v1/crates/linked-hash-map/0.5.4/download",
        type = "tar.gz",
        sha256 = "7fb9b38af92608140b86b693604b9ffcc5824240a484d1ecd4795bacb2fe88f3",
        strip_prefix = "linked-hash-map-0.5.4",
        build_file = Label("//rules/rust/remote:BUILD.linked-hash-map-0.5.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lock_api__0_4_6",
        url = "https://crates.io/api/v1/crates/lock_api/0.4.6/download",
        type = "tar.gz",
        sha256 = "88943dd7ef4a2e5a4bfa2753aaab3013e34ce2533d1996fb18ef591e315e2b3b",
        strip_prefix = "lock_api-0.4.6",
        build_file = Label("//rules/rust/remote:BUILD.lock_api-0.4.6.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__log__0_4_14",
        url = "https://crates.io/api/v1/crates/log/0.4.14/download",
        type = "tar.gz",
        sha256 = "51b9bbe6c47d51fc3e1a9b945965946b4c44142ab8792c50835a980d362c2710",
        strip_prefix = "log-0.4.14",
        build_file = Label("//rules/rust/remote:BUILD.log-0.4.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lru__0_7_3",
        url = "https://crates.io/api/v1/crates/lru/0.7.3/download",
        type = "tar.gz",
        sha256 = "fcb87f3080f6d1d69e8c564c0fcfde1d7aa8cc451ce40cae89479111f03bc0eb",
        strip_prefix = "lru-0.7.3",
        build_file = Label("//rules/rust/remote:BUILD.lru-0.7.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__lz4_flex__0_9_2",
        url = "https://crates.io/api/v1/crates/lz4_flex/0.9.2/download",
        type = "tar.gz",
        sha256 = "42c51df9d8d4842336c835df1d85ed447c4813baa237d033d95128bf5552ad8a",
        strip_prefix = "lz4_flex-0.9.2",
        build_file = Label("//rules/rust/remote:BUILD.lz4_flex-0.9.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__maplit__1_0_2",
        url = "https://crates.io/api/v1/crates/maplit/1.0.2/download",
        type = "tar.gz",
        sha256 = "3e2e65a1a2e43cfcb47a895c4c8b10d1f4a61097f9f254f183aee60cad9c651d",
        strip_prefix = "maplit-1.0.2",
        build_file = Label("//rules/rust/remote:BUILD.maplit-1.0.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__matchers__0_1_0",
        url = "https://crates.io/api/v1/crates/matchers/0.1.0/download",
        type = "tar.gz",
        sha256 = "8263075bb86c5a1b1427b5ae862e8889656f126e9f77c484496e8b47cf5c5558",
        strip_prefix = "matchers-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.matchers-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__measure_time__0_8_0",
        url = "https://crates.io/api/v1/crates/measure_time/0.8.0/download",
        type = "tar.gz",
        sha256 = "5f07966480d8562b3622f51df0b4e3fe6ea7ddb3b48b19b0f44ef863c455bdf9",
        strip_prefix = "measure_time-0.8.0",
        build_file = Label("//rules/rust/remote:BUILD.measure_time-0.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memchr__2_4_1",
        url = "https://crates.io/api/v1/crates/memchr/2.4.1/download",
        type = "tar.gz",
        sha256 = "308cc39be01b73d0d18f82a0e7b2a3df85245f84af96fdddc5d202d27e47b86a",
        strip_prefix = "memchr-2.4.1",
        build_file = Label("//rules/rust/remote:BUILD.memchr-2.4.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memmap2__0_5_3",
        url = "https://crates.io/api/v1/crates/memmap2/0.5.3/download",
        type = "tar.gz",
        sha256 = "057a3db23999c867821a7a59feb06a578fcb03685e983dff90daf9e7d24ac08f",
        strip_prefix = "memmap2-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.memmap2-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__memoffset__0_6_5",
        url = "https://crates.io/api/v1/crates/memoffset/0.6.5/download",
        type = "tar.gz",
        sha256 = "5aa361d4faea93603064a027415f07bd8e1d5c88c9fbf68bf56a285428fd79ce",
        strip_prefix = "memoffset-0.6.5",
        build_file = Label("//rules/rust/remote:BUILD.memoffset-0.6.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__minimal_lexical__0_2_1",
        url = "https://crates.io/api/v1/crates/minimal-lexical/0.2.1/download",
        type = "tar.gz",
        sha256 = "68354c5c6bd36d73ff3feceb05efa59b6acb7626617f4962be322a825e61f79a",
        strip_prefix = "minimal-lexical-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.minimal-lexical-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__mio__0_8_2",
        url = "https://crates.io/api/v1/crates/mio/0.8.2/download",
        type = "tar.gz",
        sha256 = "52da4364ffb0e4fe33a9841a98a3f3014fb964045ce4f7a45a398243c8d6b0c9",
        strip_prefix = "mio-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.mio-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__miow__0_3_7",
        url = "https://crates.io/api/v1/crates/miow/0.3.7/download",
        type = "tar.gz",
        sha256 = "b9f1c5b025cda876f66ef43a113f91ebc9f4ccef34843000e0adf6ebbab84e21",
        strip_prefix = "miow-0.3.7",
        build_file = Label("//rules/rust/remote:BUILD.miow-0.3.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__multimap__0_8_3",
        url = "https://crates.io/api/v1/crates/multimap/0.8.3/download",
        type = "tar.gz",
        sha256 = "e5ce46fe64a9d73be07dcbe690a38ce1b293be448fd8ce1e6c1b8062c9f72c6a",
        strip_prefix = "multimap-0.8.3",
        build_file = Label("//rules/rust/remote:BUILD.multimap-0.8.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__murmurhash32__0_2_0",
        url = "https://crates.io/api/v1/crates/murmurhash32/0.2.0/download",
        type = "tar.gz",
        sha256 = "d736ff882f0e85fe9689fb23db229616c4c00aee2b3ac282f666d8f20eb25d4a",
        strip_prefix = "murmurhash32-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.murmurhash32-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__nom__7_1_1",
        url = "https://crates.io/api/v1/crates/nom/7.1.1/download",
        type = "tar.gz",
        sha256 = "a8903e5a29a317527874d0402f867152a3d21c908bb0b933e416c65e301d4c36",
        strip_prefix = "nom-7.1.1",
        build_file = Label("//rules/rust/remote:BUILD.nom-7.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ntapi__0_3_7",
        url = "https://crates.io/api/v1/crates/ntapi/0.3.7/download",
        type = "tar.gz",
        sha256 = "c28774a7fd2fbb4f0babd8237ce554b73af68021b5f695a3cebd6c59bac0980f",
        strip_prefix = "ntapi-0.3.7",
        build_file = Label("//rules/rust/remote:BUILD.ntapi-0.3.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_integer__0_1_44",
        url = "https://crates.io/api/v1/crates/num-integer/0.1.44/download",
        type = "tar.gz",
        sha256 = "d2cc698a63b549a70bc047073d2949cce27cd1c7b0a4a862d08a8031bc2801db",
        strip_prefix = "num-integer-0.1.44",
        build_file = Label("//rules/rust/remote:BUILD.num-integer-0.1.44.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_traits__0_2_14",
        url = "https://crates.io/api/v1/crates/num-traits/0.2.14/download",
        type = "tar.gz",
        sha256 = "9a64b1ec5cda2586e284722486d802acf1f7dbdc623e2bfc57e65ca1cd099290",
        strip_prefix = "num-traits-0.2.14",
        build_file = Label("//rules/rust/remote:BUILD.num-traits-0.2.14.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_cpus__1_13_1",
        url = "https://crates.io/api/v1/crates/num_cpus/1.13.1/download",
        type = "tar.gz",
        sha256 = "19e64526ebdee182341572e50e9ad03965aa510cd94427a4549448f285e957a1",
        strip_prefix = "num_cpus-1.13.1",
        build_file = Label("//rules/rust/remote:BUILD.num_cpus-1.13.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_enum__0_5_7",
        url = "https://crates.io/api/v1/crates/num_enum/0.5.7/download",
        type = "tar.gz",
        sha256 = "cf5395665662ef45796a4ff5486c5d41d29e0c09640af4c5f17fd94ee2c119c9",
        strip_prefix = "num_enum-0.5.7",
        build_file = Label("//rules/rust/remote:BUILD.num_enum-0.5.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_enum_derive__0_5_7",
        url = "https://crates.io/api/v1/crates/num_enum_derive/0.5.7/download",
        type = "tar.gz",
        sha256 = "3b0498641e53dd6ac1a4f22547548caa6864cc4933784319cd1775271c5a46ce",
        strip_prefix = "num_enum_derive-0.5.7",
        build_file = Label("//rules/rust/remote:BUILD.num_enum_derive-0.5.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__num_threads__0_1_5",
        url = "https://crates.io/api/v1/crates/num_threads/0.1.5/download",
        type = "tar.gz",
        sha256 = "aba1801fb138d8e85e11d0fc70baf4fe1cdfffda7c6cd34a854905df588e5ed0",
        strip_prefix = "num_threads-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.num_threads-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__once_cell__1_10_0",
        url = "https://crates.io/api/v1/crates/once_cell/1.10.0/download",
        type = "tar.gz",
        sha256 = "87f3e037eac156d1775da914196f0f37741a274155e34a0b7e427c35d2a2ecb9",
        strip_prefix = "once_cell-1.10.0",
        build_file = Label("//rules/rust/remote:BUILD.once_cell-1.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__opaque_debug__0_2_3",
        url = "https://crates.io/api/v1/crates/opaque-debug/0.2.3/download",
        type = "tar.gz",
        sha256 = "2839e79665f131bdb5782e51f2c6c9599c133c6098982a54c794358bf432529c",
        strip_prefix = "opaque-debug-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.opaque-debug-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__opentelemetry__0_17_0",
        url = "https://crates.io/api/v1/crates/opentelemetry/0.17.0/download",
        type = "tar.gz",
        sha256 = "6105e89802af13fdf48c49d7646d3b533a70e536d818aae7e78ba0433d01acb8",
        strip_prefix = "opentelemetry-0.17.0",
        build_file = Label("//rules/rust/remote:BUILD.opentelemetry-0.17.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__opentelemetry_prometheus__0_10_0",
        url = "https://crates.io/api/v1/crates/opentelemetry-prometheus/0.10.0/download",
        type = "tar.gz",
        sha256 = "9328977e479cebe12ce0d3fcecdaea4721d234895a9440c5b5dfd113f0594ac6",
        strip_prefix = "opentelemetry-prometheus-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.opentelemetry-prometheus-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ordered_multimap__0_3_1",
        url = "https://crates.io/api/v1/crates/ordered-multimap/0.3.1/download",
        type = "tar.gz",
        sha256 = "1c672c7ad9ec066e428c00eb917124a06f08db19e2584de982cc34b1f4c12485",
        strip_prefix = "ordered-multimap-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.ordered-multimap-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__os_str_bytes__6_0_0",
        url = "https://crates.io/api/v1/crates/os_str_bytes/6.0.0/download",
        type = "tar.gz",
        sha256 = "8e22443d1643a904602595ba1cd8f7d896afe56d26712531c5ff73a15b2fbf64",
        strip_prefix = "os_str_bytes-6.0.0",
        build_file = Label("//rules/rust/remote:BUILD.os_str_bytes-6.0.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__output_vt100__0_1_3",
        url = "https://crates.io/api/v1/crates/output_vt100/0.1.3/download",
        type = "tar.gz",
        sha256 = "628223faebab4e3e40667ee0b2336d34a5b960ff60ea743ddfdbcf7770bcfb66",
        strip_prefix = "output_vt100-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.output_vt100-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ownedbytes__0_2_0",
        url = "https://crates.io/api/v1/crates/ownedbytes/0.2.0/download",
        type = "tar.gz",
        sha256 = "0bfa208b217a39411d78b85427792e4c1bc40508acbcefd2836e765f44a5c99e",
        strip_prefix = "ownedbytes-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.ownedbytes-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot__0_11_2",
        url = "https://crates.io/api/v1/crates/parking_lot/0.11.2/download",
        type = "tar.gz",
        sha256 = "7d17b78036a60663b797adeaee46f5c9dfebb86948d1255007a1d6be0271ff99",
        strip_prefix = "parking_lot-0.11.2",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot-0.11.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot__0_12_0",
        url = "https://crates.io/api/v1/crates/parking_lot/0.12.0/download",
        type = "tar.gz",
        sha256 = "87f5ec2493a61ac0506c0f4199f99070cbe83857b0337006a30f3e6719b8ef58",
        strip_prefix = "parking_lot-0.12.0",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot-0.12.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot_core__0_8_5",
        url = "https://crates.io/api/v1/crates/parking_lot_core/0.8.5/download",
        type = "tar.gz",
        sha256 = "d76e8e1493bcac0d2766c42737f34458f1c8c50c0d23bcb24ea953affb273216",
        strip_prefix = "parking_lot_core-0.8.5",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot_core-0.8.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__parking_lot_core__0_9_1",
        url = "https://crates.io/api/v1/crates/parking_lot_core/0.9.1/download",
        type = "tar.gz",
        sha256 = "28141e0cc4143da2443301914478dc976a61ffdb3f043058310c70df2fed8954",
        strip_prefix = "parking_lot_core-0.9.1",
        build_file = Label("//rules/rust/remote:BUILD.parking_lot_core-0.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pathdiff__0_2_1",
        url = "https://crates.io/api/v1/crates/pathdiff/0.2.1/download",
        type = "tar.gz",
        sha256 = "8835116a5c179084a830efb3adc117ab007512b535bc1a21c991d3b32a6b44dd",
        strip_prefix = "pathdiff-0.2.1",
        build_file = Label("//rules/rust/remote:BUILD.pathdiff-0.2.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__percent_encoding__2_1_0",
        url = "https://crates.io/api/v1/crates/percent-encoding/2.1.0/download",
        type = "tar.gz",
        sha256 = "d4fd5641d01c8f18a23da7b6fe29298ff4b55afcccdf78973b24cf3175fee32e",
        strip_prefix = "percent-encoding-2.1.0",
        build_file = Label("//rules/rust/remote:BUILD.percent-encoding-2.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pest__2_1_3",
        url = "https://crates.io/api/v1/crates/pest/2.1.3/download",
        type = "tar.gz",
        sha256 = "10f4872ae94d7b90ae48754df22fd42ad52ce740b8f370b03da4835417403e53",
        strip_prefix = "pest-2.1.3",
        build_file = Label("//rules/rust/remote:BUILD.pest-2.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pest_derive__2_1_0",
        url = "https://crates.io/api/v1/crates/pest_derive/2.1.0/download",
        type = "tar.gz",
        sha256 = "833d1ae558dc601e9a60366421196a8d94bc0ac980476d0b67e1d0988d72b2d0",
        strip_prefix = "pest_derive-2.1.0",
        build_file = Label("//rules/rust/remote:BUILD.pest_derive-2.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pest_generator__2_1_3",
        url = "https://crates.io/api/v1/crates/pest_generator/2.1.3/download",
        type = "tar.gz",
        sha256 = "99b8db626e31e5b81787b9783425769681b347011cc59471e33ea46d2ea0cf55",
        strip_prefix = "pest_generator-2.1.3",
        build_file = Label("//rules/rust/remote:BUILD.pest_generator-2.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pest_meta__2_1_3",
        url = "https://crates.io/api/v1/crates/pest_meta/2.1.3/download",
        type = "tar.gz",
        sha256 = "54be6e404f5317079812fc8f9f5279de376d8856929e21c184ecf6bbd692a11d",
        strip_prefix = "pest_meta-2.1.3",
        build_file = Label("//rules/rust/remote:BUILD.pest_meta-2.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__petgraph__0_6_0",
        url = "https://crates.io/api/v1/crates/petgraph/0.6.0/download",
        type = "tar.gz",
        sha256 = "4a13a2fa9d0b63e5f22328828741e523766fff0ee9e779316902290dff3f824f",
        strip_prefix = "petgraph-0.6.0",
        build_file = Label("//rules/rust/remote:BUILD.petgraph-0.6.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project__1_0_10",
        url = "https://crates.io/api/v1/crates/pin-project/1.0.10/download",
        type = "tar.gz",
        sha256 = "58ad3879ad3baf4e44784bc6a718a8698867bb991f8ce24d1bcbe2cfb4c3a75e",
        strip_prefix = "pin-project-1.0.10",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-1.0.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_internal__1_0_10",
        url = "https://crates.io/api/v1/crates/pin-project-internal/1.0.10/download",
        type = "tar.gz",
        sha256 = "744b6f092ba29c3650faf274db506afd39944f48420f6c86b17cfe0ee1cb36bb",
        strip_prefix = "pin-project-internal-1.0.10",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-internal-1.0.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_project_lite__0_2_8",
        url = "https://crates.io/api/v1/crates/pin-project-lite/0.2.8/download",
        type = "tar.gz",
        sha256 = "e280fbe77cc62c91527259e9442153f4688736748d24660126286329742b4c6c",
        strip_prefix = "pin-project-lite-0.2.8",
        build_file = Label("//rules/rust/remote:BUILD.pin-project-lite-0.2.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pin_utils__0_1_0",
        url = "https://crates.io/api/v1/crates/pin-utils/0.1.0/download",
        type = "tar.gz",
        sha256 = "8b870d8c151b6f2fb93e84a13146138f05d02ed11c7e7c54f8826aaaf7c9f184",
        strip_prefix = "pin-utils-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.pin-utils-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pkg_config__0_3_24",
        url = "https://crates.io/api/v1/crates/pkg-config/0.3.24/download",
        type = "tar.gz",
        sha256 = "58893f751c9b0412871a09abd62ecd2a00298c6c83befa223ef98c52aef40cbe",
        strip_prefix = "pkg-config-0.3.24",
        build_file = Label("//rules/rust/remote:BUILD.pkg-config-0.3.24.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ppv_lite86__0_2_16",
        url = "https://crates.io/api/v1/crates/ppv-lite86/0.2.16/download",
        type = "tar.gz",
        sha256 = "eb9f9e6e233e5c4a35559a617bf40a4ec447db2e84c20b55a6f83167b7e57872",
        strip_prefix = "ppv-lite86-0.2.16",
        build_file = Label("//rules/rust/remote:BUILD.ppv-lite86-0.2.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__pretty_assertions__1_2_0",
        url = "https://crates.io/api/v1/crates/pretty_assertions/1.2.0/download",
        type = "tar.gz",
        sha256 = "57c038cb5319b9c704bf9c227c261d275bfec0ad438118a2787ce47944fb228b",
        strip_prefix = "pretty_assertions-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.pretty_assertions-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro_crate__1_1_3",
        url = "https://crates.io/api/v1/crates/proc-macro-crate/1.1.3/download",
        type = "tar.gz",
        sha256 = "e17d47ce914bf4de440332250b0edd23ce48c005f59fab39d3335866b114f11a",
        strip_prefix = "proc-macro-crate-1.1.3",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro-crate-1.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__proc_macro2__1_0_36",
        url = "https://crates.io/api/v1/crates/proc-macro2/1.0.36/download",
        type = "tar.gz",
        sha256 = "c7342d5883fbccae1cc37a2353b09c87c9b0f3afd73f5fb9bba687a1f733b029",
        strip_prefix = "proc-macro2-1.0.36",
        build_file = Label("//rules/rust/remote:BUILD.proc-macro2-1.0.36.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__prometheus__0_13_0",
        url = "https://crates.io/api/v1/crates/prometheus/0.13.0/download",
        type = "tar.gz",
        sha256 = "b7f64969ffd5dd8f39bd57a68ac53c163a095ed9d0fb707146da1b27025a3504",
        strip_prefix = "prometheus-0.13.0",
        build_file = Label("//rules/rust/remote:BUILD.prometheus-0.13.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__prost__0_9_0",
        url = "https://crates.io/api/v1/crates/prost/0.9.0/download",
        type = "tar.gz",
        sha256 = "444879275cb4fd84958b1a1d5420d15e6fcf7c235fe47f053c9c2a80aceb6001",
        strip_prefix = "prost-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.prost-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__prost_build__0_9_0",
        url = "https://crates.io/api/v1/crates/prost-build/0.9.0/download",
        type = "tar.gz",
        sha256 = "62941722fb675d463659e49c4f3fe1fe792ff24fe5bbaa9c08cd3b98a1c354f5",
        strip_prefix = "prost-build-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.prost-build-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__prost_derive__0_9_0",
        url = "https://crates.io/api/v1/crates/prost-derive/0.9.0/download",
        type = "tar.gz",
        sha256 = "f9cc1a3263e07e0bf68e96268f37665207b49560d98739662cdfaae215c720fe",
        strip_prefix = "prost-derive-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.prost-derive-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__prost_types__0_9_0",
        url = "https://crates.io/api/v1/crates/prost-types/0.9.0/download",
        type = "tar.gz",
        sha256 = "534b7a0e836e3c482d2693070f982e39e7611da9695d4d1f5a4b186b51faef0a",
        strip_prefix = "prost-types-0.9.0",
        build_file = Label("//rules/rust/remote:BUILD.prost-types-0.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__protobuf__2_27_1",
        url = "https://crates.io/api/v1/crates/protobuf/2.27.1/download",
        type = "tar.gz",
        sha256 = "cf7e6d18738ecd0902d30d1ad232c9125985a3422929b16c65517b38adc14f96",
        strip_prefix = "protobuf-2.27.1",
        build_file = Label("//rules/rust/remote:BUILD.protobuf-2.27.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__quote__1_0_16",
        url = "https://crates.io/api/v1/crates/quote/1.0.16/download",
        type = "tar.gz",
        sha256 = "b4af2ec4714533fcdf07e886f17025ace8b997b9ce51204ee69b6da831c3da57",
        strip_prefix = "quote-1.0.16",
        build_file = Label("//rules/rust/remote:BUILD.quote-1.0.16.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand__0_8_5",
        url = "https://crates.io/api/v1/crates/rand/0.8.5/download",
        type = "tar.gz",
        sha256 = "34af8d1a0e25924bc5b7c43c079c942339d8f0a8b57c39049bef581b46327404",
        strip_prefix = "rand-0.8.5",
        build_file = Label("//rules/rust/remote:BUILD.rand-0.8.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_chacha__0_3_1",
        url = "https://crates.io/api/v1/crates/rand_chacha/0.3.1/download",
        type = "tar.gz",
        sha256 = "e6c10a63a0fa32252be49d21e7709d4d4baf8d231c2dbce1eaa8141b9b127d88",
        strip_prefix = "rand_chacha-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.rand_chacha-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rand_core__0_6_3",
        url = "https://crates.io/api/v1/crates/rand_core/0.6.3/download",
        type = "tar.gz",
        sha256 = "d34f1408f55294453790c48b2f1ebbb1c5b4b7563eb1f418bcfcfdbb06ebb4e7",
        strip_prefix = "rand_core-0.6.3",
        build_file = Label("//rules/rust/remote:BUILD.rand_core-0.6.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rayon__1_5_1",
        url = "https://crates.io/api/v1/crates/rayon/1.5.1/download",
        type = "tar.gz",
        sha256 = "c06aca804d41dbc8ba42dfd964f0d01334eceb64314b9ecf7c5fad5188a06d90",
        strip_prefix = "rayon-1.5.1",
        build_file = Label("//rules/rust/remote:BUILD.rayon-1.5.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rayon_core__1_9_1",
        url = "https://crates.io/api/v1/crates/rayon-core/1.9.1/download",
        type = "tar.gz",
        sha256 = "d78120e2c850279833f1dd3582f730c4ab53ed95aeaaaa862a2a5c71b1656d8e",
        strip_prefix = "rayon-core-1.9.1",
        build_file = Label("//rules/rust/remote:BUILD.rayon-core-1.9.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rdkafka__0_28_0",
        url = "https://crates.io/api/v1/crates/rdkafka/0.28.0/download",
        type = "tar.gz",
        sha256 = "1de127f294f2dba488ed46760b129d5ecbeabbd337ccbf3739cb29d50db2161c",
        strip_prefix = "rdkafka-0.28.0",
        build_file = Label("//rules/rust/remote:BUILD.rdkafka-0.28.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rdkafka_sys__4_2_0_1_8_2",
        url = "https://crates.io/api/v1/crates/rdkafka-sys/4.2.0+1.8.2/download",
        type = "tar.gz",
        sha256 = "9e542c6863b04ce0fa0c5719bc6b7b348cf8dd21af1bb03c9db5f9805b2a6473",
        strip_prefix = "rdkafka-sys-4.2.0+1.8.2",
        build_file = Label("//rules/rust/remote:BUILD.rdkafka-sys-4.2.0+1.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__redox_syscall__0_2_11",
        url = "https://crates.io/api/v1/crates/redox_syscall/0.2.11/download",
        type = "tar.gz",
        sha256 = "8380fe0152551244f0747b1bf41737e0f8a74f97a14ccefd1148187271634f3c",
        strip_prefix = "redox_syscall-0.2.11",
        build_file = Label("//rules/rust/remote:BUILD.redox_syscall-0.2.11.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex__1_5_5",
        url = "https://crates.io/api/v1/crates/regex/1.5.5/download",
        type = "tar.gz",
        sha256 = "1a11647b6b25ff05a515cb92c365cec08801e83423a235b51e231e1808747286",
        strip_prefix = "regex-1.5.5",
        build_file = Label("//rules/rust/remote:BUILD.regex-1.5.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_automata__0_1_10",
        url = "https://crates.io/api/v1/crates/regex-automata/0.1.10/download",
        type = "tar.gz",
        sha256 = "6c230d73fb8d8c1b9c0b3135c5142a8acee3a0558fb8db5cf1cb65f8d7862132",
        strip_prefix = "regex-automata-0.1.10",
        build_file = Label("//rules/rust/remote:BUILD.regex-automata-0.1.10.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_syntax__0_4_2",
        url = "https://crates.io/api/v1/crates/regex-syntax/0.4.2/download",
        type = "tar.gz",
        sha256 = "8e931c58b93d86f080c734bfd2bce7dd0079ae2331235818133c8be7f422e20e",
        strip_prefix = "regex-syntax-0.4.2",
        build_file = Label("//rules/rust/remote:BUILD.regex-syntax-0.4.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__regex_syntax__0_6_25",
        url = "https://crates.io/api/v1/crates/regex-syntax/0.6.25/download",
        type = "tar.gz",
        sha256 = "f497285884f3fcff424ffc933e56d7cbca511def0c9831a7f9b5f6153e3cc89b",
        strip_prefix = "regex-syntax-0.6.25",
        build_file = Label("//rules/rust/remote:BUILD.regex-syntax-0.6.25.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__remove_dir_all__0_5_3",
        url = "https://crates.io/api/v1/crates/remove_dir_all/0.5.3/download",
        type = "tar.gz",
        sha256 = "3acd125665422973a33ac9d3dd2df85edad0f4ae9b00dafb1a05e43a9f5ef8e7",
        strip_prefix = "remove_dir_all-0.5.3",
        build_file = Label("//rules/rust/remote:BUILD.remove_dir_all-0.5.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ron__0_7_0",
        url = "https://crates.io/api/v1/crates/ron/0.7.0/download",
        type = "tar.gz",
        sha256 = "1b861ecaade43ac97886a512b360d01d66be9f41f3c61088b42cedf92e03d678",
        strip_prefix = "ron-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.ron-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_ini__0_17_0",
        url = "https://crates.io/api/v1/crates/rust-ini/0.17.0/download",
        type = "tar.gz",
        sha256 = "63471c4aa97a1cf8332a5f97709a79a4234698de6a1f5087faf66f2dae810e22",
        strip_prefix = "rust-ini-0.17.0",
        build_file = Label("//rules/rust/remote:BUILD.rust-ini-0.17.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__rust_stemmers__1_2_0",
        url = "https://crates.io/api/v1/crates/rust-stemmers/1.2.0/download",
        type = "tar.gz",
        sha256 = "e46a2036019fdb888131db7a4c847a1063a7493f971ed94ea82c67eada63ca54",
        strip_prefix = "rust-stemmers-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.rust-stemmers-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ryu__1_0_9",
        url = "https://crates.io/api/v1/crates/ryu/1.0.9/download",
        type = "tar.gz",
        sha256 = "73b4b750c782965c211b42f022f59af1fbceabdd026623714f104152f1ec149f",
        strip_prefix = "ryu-1.0.9",
        build_file = Label("//rules/rust/remote:BUILD.ryu-1.0.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__scopeguard__1_1_0",
        url = "https://crates.io/api/v1/crates/scopeguard/1.1.0/download",
        type = "tar.gz",
        sha256 = "d29ab0c6d3fc0ee92fe66e2d99f700eab17a8d57d1c1d3b748380fb20baa78cd",
        strip_prefix = "scopeguard-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.scopeguard-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde__1_0_136",
        url = "https://crates.io/api/v1/crates/serde/1.0.136/download",
        type = "tar.gz",
        sha256 = "ce31e24b01e1e524df96f1c2fdd054405f8d7376249a5110886fb4b658484789",
        strip_prefix = "serde-1.0.136",
        build_file = Label("//rules/rust/remote:BUILD.serde-1.0.136.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_derive__1_0_136",
        url = "https://crates.io/api/v1/crates/serde_derive/1.0.136/download",
        type = "tar.gz",
        sha256 = "08597e7152fcd306f41838ed3e37be9eaeed2b61c42e2117266a554fab4662f9",
        strip_prefix = "serde_derive-1.0.136",
        build_file = Label("//rules/rust/remote:BUILD.serde_derive-1.0.136.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_json__1_0_79",
        url = "https://crates.io/api/v1/crates/serde_json/1.0.79/download",
        type = "tar.gz",
        sha256 = "8e8d9fa5c3b304765ce1fd9c4c8a3de2c8db365a5b91be52f186efc675681d95",
        strip_prefix = "serde_json-1.0.79",
        build_file = Label("//rules/rust/remote:BUILD.serde_json-1.0.79.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__serde_yaml__0_8_23",
        url = "https://crates.io/api/v1/crates/serde_yaml/0.8.23/download",
        type = "tar.gz",
        sha256 = "a4a521f2940385c165a24ee286aa8599633d162077a54bdcae2a6fd5a7bfa7a0",
        strip_prefix = "serde_yaml-0.8.23",
        build_file = Label("//rules/rust/remote:BUILD.serde_yaml-0.8.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sha_1__0_8_2",
        url = "https://crates.io/api/v1/crates/sha-1/0.8.2/download",
        type = "tar.gz",
        sha256 = "f7d94d0bede923b3cea61f3f1ff57ff8cdfd77b400fb8f9998949e0cf04163df",
        strip_prefix = "sha-1-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.sha-1-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__sharded_slab__0_1_4",
        url = "https://crates.io/api/v1/crates/sharded-slab/0.1.4/download",
        type = "tar.gz",
        sha256 = "900fba806f70c630b0a382d0d825e17a0f19fcd059a2ade1ff237bcddf446b31",
        strip_prefix = "sharded-slab-0.1.4",
        build_file = Label("//rules/rust/remote:BUILD.sharded-slab-0.1.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook__0_3_13",
        url = "https://crates.io/api/v1/crates/signal-hook/0.3.13/download",
        type = "tar.gz",
        sha256 = "647c97df271007dcea485bb74ffdb57f2e683f1306c854f468a0c244badabf2d",
        strip_prefix = "signal-hook-0.3.13",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-0.3.13.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__signal_hook_registry__1_4_0",
        url = "https://crates.io/api/v1/crates/signal-hook-registry/1.4.0/download",
        type = "tar.gz",
        sha256 = "e51e73328dc4ac0c7ccbda3a494dfa03df1de2f46018127f60c693f2648455b0",
        strip_prefix = "signal-hook-registry-1.4.0",
        build_file = Label("//rules/rust/remote:BUILD.signal-hook-registry-1.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__slab__0_4_5",
        url = "https://crates.io/api/v1/crates/slab/0.4.5/download",
        type = "tar.gz",
        sha256 = "9def91fd1e018fe007022791f865d0ccc9b3a0d5001e01aabb8b40e46000afb5",
        strip_prefix = "slab-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.slab-0.4.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__smallvec__1_8_0",
        url = "https://crates.io/api/v1/crates/smallvec/1.8.0/download",
        type = "tar.gz",
        sha256 = "f2dd574626839106c320a323308629dcb1acfc96e32a8cba364ddc61ac23ee83",
        strip_prefix = "smallvec-1.8.0",
        build_file = Label("//rules/rust/remote:BUILD.smallvec-1.8.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__smawk__0_3_1",
        url = "https://crates.io/api/v1/crates/smawk/0.3.1/download",
        type = "tar.gz",
        sha256 = "f67ad224767faa3c7d8b6d91985b78e70a1324408abcb1cfcc2be4c06bc06043",
        strip_prefix = "smawk-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.smawk-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__socket2__0_4_4",
        url = "https://crates.io/api/v1/crates/socket2/0.4.4/download",
        type = "tar.gz",
        sha256 = "66d72b759436ae32898a2af0a14218dbf55efde3feeb170eb623637db85ee1e0",
        strip_prefix = "socket2-0.4.4",
        build_file = Label("//rules/rust/remote:BUILD.socket2-0.4.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__stable_deref_trait__1_2_0",
        url = "https://crates.io/api/v1/crates/stable_deref_trait/1.2.0/download",
        type = "tar.gz",
        sha256 = "a8f112729512f8e442d81f95a8a7ddf2b7c6b8a1a6f509a95864142b30cab2d3",
        strip_prefix = "stable_deref_trait-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.stable_deref_trait-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__static_assertions__1_1_0",
        url = "https://crates.io/api/v1/crates/static_assertions/1.1.0/download",
        type = "tar.gz",
        sha256 = "a2eb9349b6444b326872e140eb1cf5e7c522154d69e7a0ffb0fb81c06b37543f",
        strip_prefix = "static_assertions-1.1.0",
        build_file = Label("//rules/rust/remote:BUILD.static_assertions-1.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__strsim__0_10_0",
        url = "https://crates.io/api/v1/crates/strsim/0.10.0/download",
        type = "tar.gz",
        sha256 = "73473c0e59e6d5812c5dfe2a064a6444949f089e20eec9a2e5506596494e4623",
        strip_prefix = "strsim-0.10.0",
        build_file = Label("//rules/rust/remote:BUILD.strsim-0.10.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__syn__1_0_89",
        url = "https://crates.io/api/v1/crates/syn/1.0.89/download",
        type = "tar.gz",
        sha256 = "ea297be220d52398dcc07ce15a209fce436d361735ac1db700cab3b6cdfb9f54",
        strip_prefix = "syn-1.0.89",
        build_file = Label("//rules/rust/remote:BUILD.syn-1.0.89.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy__0_17_0",
        url = "https://crates.io/api/v1/crates/tantivy/0.17.0/download",
        type = "tar.gz",
        sha256 = "264c2549892aa83975386a924ef8d0b8e909674c837d37ea58b4bd8739495c6e",
        strip_prefix = "tantivy-0.17.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-0.17.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_bitpacker__0_1_1",
        url = "https://crates.io/api/v1/crates/tantivy-bitpacker/0.1.1/download",
        type = "tar.gz",
        sha256 = "66d10a5ed75437a4f6bbbba67601cd5adab8d71f5188b677055381f0f36064f2",
        strip_prefix = "tantivy-bitpacker-0.1.1",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-bitpacker-0.1.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_common__0_1_0",
        url = "https://crates.io/api/v1/crates/tantivy-common/0.1.0/download",
        type = "tar.gz",
        sha256 = "760e44073e328f4ea3f38660da9ba2598a19ad5ad4149cfb89ad89b4d5ee88d9",
        strip_prefix = "tantivy-common-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-common-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_common__0_2_0",
        url = "https://crates.io/api/v1/crates/tantivy-common/0.2.0/download",
        type = "tar.gz",
        sha256 = "2078cd12c7e46eb2cd66ec813eac8472e0f9dfe816f26159effceffd2dbe4793",
        strip_prefix = "tantivy-common-0.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-common-0.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_fst__0_3_0",
        url = "https://crates.io/api/v1/crates/tantivy-fst/0.3.0/download",
        type = "tar.gz",
        sha256 = "cb20cdc0d83e9184560bdde9cd60142dbb4af2e0f770e88fce45770495224205",
        strip_prefix = "tantivy-fst-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-fst-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tantivy_query_grammar__0_15_0",
        url = "https://crates.io/api/v1/crates/tantivy-query-grammar/0.15.0/download",
        type = "tar.gz",
        sha256 = "466e0218472a9b276a73e38b2571ac02f9a1b270b4481c9cd8cc23a63d1307e9",
        strip_prefix = "tantivy-query-grammar-0.15.0",
        build_file = Label("//rules/rust/remote:BUILD.tantivy-query-grammar-0.15.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tempfile__3_3_0",
        url = "https://crates.io/api/v1/crates/tempfile/3.3.0/download",
        type = "tar.gz",
        sha256 = "5cdb1ef4eaeeaddc8fbd371e5017057064af0911902ef36b39801f67cc6d79e4",
        strip_prefix = "tempfile-3.3.0",
        build_file = Label("//rules/rust/remote:BUILD.tempfile-3.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__termcolor__1_1_3",
        url = "https://crates.io/api/v1/crates/termcolor/1.1.3/download",
        type = "tar.gz",
        sha256 = "bab24d30b911b2376f3a13cc2cd443142f0c81dda04c118693e35b3835757755",
        strip_prefix = "termcolor-1.1.3",
        build_file = Label("//rules/rust/remote:BUILD.termcolor-1.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__textwrap__0_15_0",
        url = "https://crates.io/api/v1/crates/textwrap/0.15.0/download",
        type = "tar.gz",
        sha256 = "b1141d4d61095b28419e22cb0bbf02755f5e54e0526f97f1e3d1d160e60885fb",
        strip_prefix = "textwrap-0.15.0",
        build_file = Label("//rules/rust/remote:BUILD.textwrap-0.15.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thiserror__1_0_30",
        url = "https://crates.io/api/v1/crates/thiserror/1.0.30/download",
        type = "tar.gz",
        sha256 = "854babe52e4df1653706b98fcfc05843010039b406875930a70e4d9644e5c417",
        strip_prefix = "thiserror-1.0.30",
        build_file = Label("//rules/rust/remote:BUILD.thiserror-1.0.30.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thiserror_impl__1_0_30",
        url = "https://crates.io/api/v1/crates/thiserror-impl/1.0.30/download",
        type = "tar.gz",
        sha256 = "aa32fd3f627f367fe16f893e2597ae3c05020f8bba2666a4e6ea73d377e5714b",
        strip_prefix = "thiserror-impl-1.0.30",
        build_file = Label("//rules/rust/remote:BUILD.thiserror-impl-1.0.30.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__thread_local__1_1_4",
        url = "https://crates.io/api/v1/crates/thread_local/1.1.4/download",
        type = "tar.gz",
        sha256 = "5516c27b78311c50bf42c071425c560ac799b11c30b31f87e3081965fe5e0180",
        strip_prefix = "thread_local-1.1.4",
        build_file = Label("//rules/rust/remote:BUILD.thread_local-1.1.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time__0_1_44",
        url = "https://crates.io/api/v1/crates/time/0.1.44/download",
        type = "tar.gz",
        sha256 = "6db9e6914ab8b1ae1c260a4ae7a49b6c5611b40328a735b21862567685e73255",
        strip_prefix = "time-0.1.44",
        build_file = Label("//rules/rust/remote:BUILD.time-0.1.44.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__time__0_3_7",
        url = "https://crates.io/api/v1/crates/time/0.3.7/download",
        type = "tar.gz",
        sha256 = "004cbc98f30fa233c61a38bc77e96a9106e65c88f2d3bef182ae952027e5753d",
        strip_prefix = "time-0.3.7",
        build_file = Label("//rules/rust/remote:BUILD.time-0.3.7.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio__1_17_0",
        url = "https://crates.io/api/v1/crates/tokio/1.17.0/download",
        type = "tar.gz",
        sha256 = "2af73ac49756f3f7c01172e34a23e5d0216f6c32333757c2c61feb2bbff5a5ee",
        strip_prefix = "tokio-1.17.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-1.17.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_io_timeout__1_2_0",
        url = "https://crates.io/api/v1/crates/tokio-io-timeout/1.2.0/download",
        type = "tar.gz",
        sha256 = "30b74022ada614a1b4834de765f9bb43877f910cc8ce4be40e89042c9223a8bf",
        strip_prefix = "tokio-io-timeout-1.2.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-io-timeout-1.2.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_macros__1_7_0",
        url = "https://crates.io/api/v1/crates/tokio-macros/1.7.0/download",
        type = "tar.gz",
        sha256 = "b557f72f448c511a979e2564e55d74e6c4432fc96ff4f6241bc6bded342643b7",
        strip_prefix = "tokio-macros-1.7.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-macros-1.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_stream__0_1_8",
        url = "https://crates.io/api/v1/crates/tokio-stream/0.1.8/download",
        type = "tar.gz",
        sha256 = "50145484efff8818b5ccd256697f36863f587da82cf8b409c53adf1e840798e3",
        strip_prefix = "tokio-stream-0.1.8",
        build_file = Label("//rules/rust/remote:BUILD.tokio-stream-0.1.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_6_9",
        url = "https://crates.io/api/v1/crates/tokio-util/0.6.9/download",
        type = "tar.gz",
        sha256 = "9e99e1983e5d376cd8eb4b66604d2e99e79f5bd988c3055891dcd8c9e2604cc0",
        strip_prefix = "tokio-util-0.6.9",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.6.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tokio_util__0_7_0",
        url = "https://crates.io/api/v1/crates/tokio-util/0.7.0/download",
        type = "tar.gz",
        sha256 = "64910e1b9c1901aaf5375561e35b9c057d95ff41a44ede043a03e09279eabaf1",
        strip_prefix = "tokio-util-0.7.0",
        build_file = Label("//rules/rust/remote:BUILD.tokio-util-0.7.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__toml__0_5_8",
        url = "https://crates.io/api/v1/crates/toml/0.5.8/download",
        type = "tar.gz",
        sha256 = "a31142970826733df8241ef35dc040ef98c679ab14d7c3e54d827099b3acecaa",
        strip_prefix = "toml-0.5.8",
        build_file = Label("//rules/rust/remote:BUILD.toml-0.5.8.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tonic__0_6_2",
        url = "https://crates.io/api/v1/crates/tonic/0.6.2/download",
        type = "tar.gz",
        sha256 = "ff08f4649d10a70ffa3522ca559031285d8e421d727ac85c60825761818f5d0a",
        strip_prefix = "tonic-0.6.2",
        build_file = Label("//rules/rust/remote:BUILD.tonic-0.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tonic_build__0_6_2",
        url = "https://crates.io/api/v1/crates/tonic-build/0.6.2/download",
        type = "tar.gz",
        sha256 = "9403f1bafde247186684b230dc6f38b5cd514584e8bec1dd32514be4745fa757",
        strip_prefix = "tonic-build-0.6.2",
        build_file = Label("//rules/rust/remote:BUILD.tonic-build-0.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tower__0_4_12",
        url = "https://crates.io/api/v1/crates/tower/0.4.12/download",
        type = "tar.gz",
        sha256 = "9a89fd63ad6adf737582df5db40d286574513c69a11dac5214dc3b5603d6713e",
        strip_prefix = "tower-0.4.12",
        build_file = Label("//rules/rust/remote:BUILD.tower-0.4.12.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tower_http__0_2_5",
        url = "https://crates.io/api/v1/crates/tower-http/0.2.5/download",
        type = "tar.gz",
        sha256 = "aba3f3efabf7fb41fae8534fc20a817013dd1c12cb45441efb6c82e6556b4cd8",
        strip_prefix = "tower-http-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.tower-http-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tower_layer__0_3_1",
        url = "https://crates.io/api/v1/crates/tower-layer/0.3.1/download",
        type = "tar.gz",
        sha256 = "343bc9466d3fe6b0f960ef45960509f84480bf4fd96f92901afe7ff3df9d3a62",
        strip_prefix = "tower-layer-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.tower-layer-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tower_service__0_3_1",
        url = "https://crates.io/api/v1/crates/tower-service/0.3.1/download",
        type = "tar.gz",
        sha256 = "360dfd1d6d30e05fda32ace2c8c70e9c0a9da713275777f5a4dbb8a1893930c6",
        strip_prefix = "tower-service-0.3.1",
        build_file = Label("//rules/rust/remote:BUILD.tower-service-0.3.1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing__0_1_32",
        url = "https://crates.io/api/v1/crates/tracing/0.1.32/download",
        type = "tar.gz",
        sha256 = "4a1bdf54a7c28a2bbf701e1d2233f6c77f473486b94bee4f9678da5a148dca7f",
        strip_prefix = "tracing-0.1.32",
        build_file = Label("//rules/rust/remote:BUILD.tracing-0.1.32.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_appender__0_2_2",
        url = "https://crates.io/api/v1/crates/tracing-appender/0.2.2/download",
        type = "tar.gz",
        sha256 = "09d48f71a791638519505cefafe162606f706c25592e4bde4d97600c0195312e",
        strip_prefix = "tracing-appender-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.tracing-appender-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_attributes__0_1_20",
        url = "https://crates.io/api/v1/crates/tracing-attributes/0.1.20/download",
        type = "tar.gz",
        sha256 = "2e65ce065b4b5c53e73bb28912318cb8c9e9ad3921f1d669eb0e68b4c8143a2b",
        strip_prefix = "tracing-attributes-0.1.20",
        build_file = Label("//rules/rust/remote:BUILD.tracing-attributes-0.1.20.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_core__0_1_23",
        url = "https://crates.io/api/v1/crates/tracing-core/0.1.23/download",
        type = "tar.gz",
        sha256 = "aa31669fa42c09c34d94d8165dd2012e8ff3c66aca50f3bb226b68f216f2706c",
        strip_prefix = "tracing-core-0.1.23",
        build_file = Label("//rules/rust/remote:BUILD.tracing-core-0.1.23.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_futures__0_2_5",
        url = "https://crates.io/api/v1/crates/tracing-futures/0.2.5/download",
        type = "tar.gz",
        sha256 = "97d095ae15e245a057c8e8451bab9b3ee1e1f68e9ba2b4fbc18d0ac5237835f2",
        strip_prefix = "tracing-futures-0.2.5",
        build_file = Label("//rules/rust/remote:BUILD.tracing-futures-0.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_log__0_1_2",
        url = "https://crates.io/api/v1/crates/tracing-log/0.1.2/download",
        type = "tar.gz",
        sha256 = "a6923477a48e41c1951f1999ef8bb5a3023eb723ceadafe78ffb65dc366761e3",
        strip_prefix = "tracing-log-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.tracing-log-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_serde__0_1_3",
        url = "https://crates.io/api/v1/crates/tracing-serde/0.1.3/download",
        type = "tar.gz",
        sha256 = "bc6b213177105856957181934e4920de57730fc69bf42c37ee5bb664d406d9e1",
        strip_prefix = "tracing-serde-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.tracing-serde-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__tracing_subscriber__0_3_9",
        url = "https://crates.io/api/v1/crates/tracing-subscriber/0.3.9/download",
        type = "tar.gz",
        sha256 = "9e0ab7bdc962035a87fba73f3acca9b8a8d0034c2e6f60b84aeaaddddc155dce",
        strip_prefix = "tracing-subscriber-0.3.9",
        build_file = Label("//rules/rust/remote:BUILD.tracing-subscriber-0.3.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__try_lock__0_2_3",
        url = "https://crates.io/api/v1/crates/try-lock/0.2.3/download",
        type = "tar.gz",
        sha256 = "59547bce71d9c38b83d9c0e92b6066c4253371f15005def0c30d9657f50c7642",
        strip_prefix = "try-lock-0.2.3",
        build_file = Label("//rules/rust/remote:BUILD.try-lock-0.2.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__twox_hash__1_6_2",
        url = "https://crates.io/api/v1/crates/twox-hash/1.6.2/download",
        type = "tar.gz",
        sha256 = "4ee73e6e4924fe940354b8d4d98cad5231175d615cd855b758adc658c0aac6a0",
        strip_prefix = "twox-hash-1.6.2",
        build_file = Label("//rules/rust/remote:BUILD.twox-hash-1.6.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__typenum__1_15_0",
        url = "https://crates.io/api/v1/crates/typenum/1.15.0/download",
        type = "tar.gz",
        sha256 = "dcf81ac59edc17cc8697ff311e8f5ef2d99fcbd9817b34cec66f90b6c3dfd987",
        strip_prefix = "typenum-1.15.0",
        build_file = Label("//rules/rust/remote:BUILD.typenum-1.15.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__ucd_trie__0_1_3",
        url = "https://crates.io/api/v1/crates/ucd-trie/0.1.3/download",
        type = "tar.gz",
        sha256 = "56dee185309b50d1f11bfedef0fe6d036842e3fb77413abef29f8f8d1c5d4c1c",
        strip_prefix = "ucd-trie-0.1.3",
        build_file = Label("//rules/rust/remote:BUILD.ucd-trie-0.1.3.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_linebreak__0_1_2",
        url = "https://crates.io/api/v1/crates/unicode-linebreak/0.1.2/download",
        type = "tar.gz",
        sha256 = "3a52dcaab0c48d931f7cc8ef826fa51690a08e1ea55117ef26f89864f532383f",
        strip_prefix = "unicode-linebreak-0.1.2",
        build_file = Label("//rules/rust/remote:BUILD.unicode-linebreak-0.1.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_segmentation__1_9_0",
        url = "https://crates.io/api/v1/crates/unicode-segmentation/1.9.0/download",
        type = "tar.gz",
        sha256 = "7e8820f5d777f6224dc4be3632222971ac30164d4a258d595640799554ebfd99",
        strip_prefix = "unicode-segmentation-1.9.0",
        build_file = Label("//rules/rust/remote:BUILD.unicode-segmentation-1.9.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_width__0_1_9",
        url = "https://crates.io/api/v1/crates/unicode-width/0.1.9/download",
        type = "tar.gz",
        sha256 = "3ed742d4ea2bd1176e236172c8429aaf54486e7ac098db29ffe6529e0ce50973",
        strip_prefix = "unicode-width-0.1.9",
        build_file = Label("//rules/rust/remote:BUILD.unicode-width-0.1.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__unicode_xid__0_2_2",
        url = "https://crates.io/api/v1/crates/unicode-xid/0.2.2/download",
        type = "tar.gz",
        sha256 = "8ccb82d61f80a663efe1f787a51b16b5a51e3314d6ac365b08639f52387b33f3",
        strip_prefix = "unicode-xid-0.2.2",
        build_file = Label("//rules/rust/remote:BUILD.unicode-xid-0.2.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__utf8_ranges__1_0_4",
        url = "https://crates.io/api/v1/crates/utf8-ranges/1.0.4/download",
        type = "tar.gz",
        sha256 = "b4ae116fef2b7fea257ed6440d3cfcff7f190865f170cdad00bb6465bf18ecba",
        strip_prefix = "utf8-ranges-1.0.4",
        build_file = Label("//rules/rust/remote:BUILD.utf8-ranges-1.0.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__uuid__0_8_2",
        url = "https://crates.io/api/v1/crates/uuid/0.8.2/download",
        type = "tar.gz",
        sha256 = "bc5cf98d8186244414c848017f0e2676b3fcb46807f6668a97dfe67359a3c4b7",
        strip_prefix = "uuid-0.8.2",
        build_file = Label("//rules/rust/remote:BUILD.uuid-0.8.2.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__valuable__0_1_0",
        url = "https://crates.io/api/v1/crates/valuable/0.1.0/download",
        type = "tar.gz",
        sha256 = "830b7e5d4d90034032940e4ace0d9a9a057e7a45cd94e6c007832e39edb82f6d",
        strip_prefix = "valuable-0.1.0",
        build_file = Label("//rules/rust/remote:BUILD.valuable-0.1.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__vcpkg__0_2_15",
        url = "https://crates.io/api/v1/crates/vcpkg/0.2.15/download",
        type = "tar.gz",
        sha256 = "accd4ea62f7bb7a82fe23066fb0957d48ef677f6eeb8215f372f52e48bb32426",
        strip_prefix = "vcpkg-0.2.15",
        build_file = Label("//rules/rust/remote:BUILD.vcpkg-0.2.15.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__version_check__0_9_4",
        url = "https://crates.io/api/v1/crates/version_check/0.9.4/download",
        type = "tar.gz",
        sha256 = "49874b5167b65d7193b8aba1567f5c7d93d001cafc34600cee003eda787e483f",
        strip_prefix = "version_check-0.9.4",
        build_file = Label("//rules/rust/remote:BUILD.version_check-0.9.4.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__want__0_3_0",
        url = "https://crates.io/api/v1/crates/want/0.3.0/download",
        type = "tar.gz",
        sha256 = "1ce8a968cb1cd110d136ff8b819a556d6fb6d919363c61534f6860c7eb172ba0",
        strip_prefix = "want-0.3.0",
        build_file = Label("//rules/rust/remote:BUILD.want-0.3.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasi__0_10_0_wasi_snapshot_preview1",
        url = "https://crates.io/api/v1/crates/wasi/0.10.0+wasi-snapshot-preview1/download",
        type = "tar.gz",
        sha256 = "1a143597ca7c7793eff794def352d41792a93c481eb1042423ff7ff72ba2c31f",
        strip_prefix = "wasi-0.10.0+wasi-snapshot-preview1",
        build_file = Label("//rules/rust/remote:BUILD.wasi-0.10.0+wasi-snapshot-preview1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasi__0_11_0_wasi_snapshot_preview1",
        url = "https://crates.io/api/v1/crates/wasi/0.11.0+wasi-snapshot-preview1/download",
        type = "tar.gz",
        sha256 = "9c8d87e72b64a3b4db28d11ce29237c246188f4f51057d65a7eab63b7987e423",
        strip_prefix = "wasi-0.11.0+wasi-snapshot-preview1",
        build_file = Label("//rules/rust/remote:BUILD.wasi-0.11.0+wasi-snapshot-preview1.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen__0_2_79",
        url = "https://crates.io/api/v1/crates/wasm-bindgen/0.2.79/download",
        type = "tar.gz",
        sha256 = "25f1af7423d8588a3d840681122e72e6a24ddbcb3f0ec385cac0d12d24256c06",
        strip_prefix = "wasm-bindgen-0.2.79",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-0.2.79.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_backend__0_2_79",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-backend/0.2.79/download",
        type = "tar.gz",
        sha256 = "8b21c0df030f5a177f3cba22e9bc4322695ec43e7257d865302900290bcdedca",
        strip_prefix = "wasm-bindgen-backend-0.2.79",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-backend-0.2.79.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_macro__0_2_79",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-macro/0.2.79/download",
        type = "tar.gz",
        sha256 = "2f4203d69e40a52ee523b2529a773d5ffc1dc0071801c87b3d270b471b80ed01",
        strip_prefix = "wasm-bindgen-macro-0.2.79",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-macro-0.2.79.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_macro_support__0_2_79",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-macro-support/0.2.79/download",
        type = "tar.gz",
        sha256 = "bfa8a30d46208db204854cadbb5d4baf5fcf8071ba5bf48190c3e59937962ebc",
        strip_prefix = "wasm-bindgen-macro-support-0.2.79",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-macro-support-0.2.79.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__wasm_bindgen_shared__0_2_79",
        url = "https://crates.io/api/v1/crates/wasm-bindgen-shared/0.2.79/download",
        type = "tar.gz",
        sha256 = "3d958d035c4438e28c70e4321a2911302f10135ce78a9c7834c0cab4123d06a2",
        strip_prefix = "wasm-bindgen-shared-0.2.79",
        build_file = Label("//rules/rust/remote:BUILD.wasm-bindgen-shared-0.2.79.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__which__4_2_5",
        url = "https://crates.io/api/v1/crates/which/4.2.5/download",
        type = "tar.gz",
        sha256 = "5c4fb54e6113b6a8772ee41c3404fb0301ac79604489467e0a9ce1f3e97c24ae",
        strip_prefix = "which-4.2.5",
        build_file = Label("//rules/rust/remote:BUILD.which-4.2.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi__0_3_9",
        url = "https://crates.io/api/v1/crates/winapi/0.3.9/download",
        type = "tar.gz",
        sha256 = "5c839a674fcd7a98952e593242ea400abe93992746761e38641405d28b00f419",
        strip_prefix = "winapi-0.3.9",
        build_file = Label("//rules/rust/remote:BUILD.winapi-0.3.9.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_i686_pc_windows_gnu__0_4_0",
        url = "https://crates.io/api/v1/crates/winapi-i686-pc-windows-gnu/0.4.0/download",
        type = "tar.gz",
        sha256 = "ac3b87c63620426dd9b991e5ce0329eff545bccbbb34f3be09ff6fb6ab51b7b6",
        strip_prefix = "winapi-i686-pc-windows-gnu-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.winapi-i686-pc-windows-gnu-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_util__0_1_5",
        url = "https://crates.io/api/v1/crates/winapi-util/0.1.5/download",
        type = "tar.gz",
        sha256 = "70ec6ce85bb158151cae5e5c87f95a8e97d2c0c4b001223f33a334e3ce5de178",
        strip_prefix = "winapi-util-0.1.5",
        build_file = Label("//rules/rust/remote:BUILD.winapi-util-0.1.5.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__winapi_x86_64_pc_windows_gnu__0_4_0",
        url = "https://crates.io/api/v1/crates/winapi-x86_64-pc-windows-gnu/0.4.0/download",
        type = "tar.gz",
        sha256 = "712e227841d057c1ee1cd2fb22fa7e5a5461ae8e48fa2ca79ec42cfc1931183f",
        strip_prefix = "winapi-x86_64-pc-windows-gnu-0.4.0",
        build_file = Label("//rules/rust/remote:BUILD.winapi-x86_64-pc-windows-gnu-0.4.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__windows_sys__0_32_0",
        url = "https://crates.io/api/v1/crates/windows-sys/0.32.0/download",
        type = "tar.gz",
        sha256 = "3df6e476185f92a12c072be4a189a0210dcdcf512a1891d6dff9edb874deadc6",
        strip_prefix = "windows-sys-0.32.0",
        build_file = Label("//rules/rust/remote:BUILD.windows-sys-0.32.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__windows_aarch64_msvc__0_32_0",
        url = "https://crates.io/api/v1/crates/windows_aarch64_msvc/0.32.0/download",
        type = "tar.gz",
        sha256 = "d8e92753b1c443191654ec532f14c199742964a061be25d77d7a96f09db20bf5",
        strip_prefix = "windows_aarch64_msvc-0.32.0",
        build_file = Label("//rules/rust/remote:BUILD.windows_aarch64_msvc-0.32.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__windows_i686_gnu__0_32_0",
        url = "https://crates.io/api/v1/crates/windows_i686_gnu/0.32.0/download",
        type = "tar.gz",
        sha256 = "6a711c68811799e017b6038e0922cb27a5e2f43a2ddb609fe0b6f3eeda9de615",
        strip_prefix = "windows_i686_gnu-0.32.0",
        build_file = Label("//rules/rust/remote:BUILD.windows_i686_gnu-0.32.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__windows_i686_msvc__0_32_0",
        url = "https://crates.io/api/v1/crates/windows_i686_msvc/0.32.0/download",
        type = "tar.gz",
        sha256 = "146c11bb1a02615db74680b32a68e2d61f553cc24c4eb5b4ca10311740e44172",
        strip_prefix = "windows_i686_msvc-0.32.0",
        build_file = Label("//rules/rust/remote:BUILD.windows_i686_msvc-0.32.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__windows_x86_64_gnu__0_32_0",
        url = "https://crates.io/api/v1/crates/windows_x86_64_gnu/0.32.0/download",
        type = "tar.gz",
        sha256 = "c912b12f7454c6620635bbff3450962753834be2a594819bd5e945af18ec64bc",
        strip_prefix = "windows_x86_64_gnu-0.32.0",
        build_file = Label("//rules/rust/remote:BUILD.windows_x86_64_gnu-0.32.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__windows_x86_64_msvc__0_32_0",
        url = "https://crates.io/api/v1/crates/windows_x86_64_msvc/0.32.0/download",
        type = "tar.gz",
        sha256 = "504a2476202769977a040c6364301a3f65d0cc9e3fb08600b2bda150a0488316",
        strip_prefix = "windows_x86_64_msvc-0.32.0",
        build_file = Label("//rules/rust/remote:BUILD.windows_x86_64_msvc-0.32.0.bazel"),
    )

    maybe(
        http_archive,
        name = "raze__yaml_rust__0_4_5",
        url = "https://crates.io/api/v1/crates/yaml-rust/0.4.5/download",
        type = "tar.gz",
        sha256 = "56c1936c4cc7a1c9ab21a1ebb602eb942ba868cbd44a99cb7cdc5892335e1c85",
        strip_prefix = "yaml-rust-0.4.5",
        build_file = Label("//rules/rust/remote:BUILD.yaml-rust-0.4.5.bazel"),
    )
