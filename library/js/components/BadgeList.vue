<template lang="pug">
  b-container
    b-modal(ref="newElementModal", :title="'New ' + typeName", @ok="handleAddElementOk", @cancel="handleAddElementCancel", @shown="$refs.newElement.focus()")
      p.text-modal
        b-form-input.form-control-sm(ref="newElement", v-model="newElement")
    b-badge.ml-2(v-for="(element, elementIndex) of value", :key="elementIndex")
      span {{ getDisplayName(element) }}
      i.ml-1.fa.fa-sm.fa-remove(@click="deleteElement(elementIndex)", v-if="mutable")
    b-badge.ml-2(@click="handleAddElementInit", variant="danger", v-if="mutable")
      i.fa.fa-md.fa-plus
</template>

<script>

import BaseList from '~/library/js/components/BaseList'

export default {
  name: 'BadgeList',
  extends: BaseList
}
</script>
