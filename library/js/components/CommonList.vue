<template lang="pug">
  b-container
    b-modal(ref="newElementModal", :title="'New ' + typeName", @ok="handleAddElementOk", @cancel="handleAddElementCancel", @shown="$refs.newElement.focus()")
      p.text-modal
        b-form-input.form-control-sm(ref="newElement", v-model="newElement")
    div(v-for="(element, elementIndex) of value", :key="elementIndex")
      span {{ getDisplayName(element) }}
      i.ml-1.fa.fa-sm.fa-remove.float-right(@click="deleteElement(elementIndex)", v-if="mutable")
      hr
    b-button.btn-sm.float-right(@click="handleAddElementInit", variant="primary", v-if="mutable") Add
</template>

<script>

import BaseList from '~/library/js/components/BaseList'

export default {
  name: 'CommonList',
  extends: BaseList
}
</script>
