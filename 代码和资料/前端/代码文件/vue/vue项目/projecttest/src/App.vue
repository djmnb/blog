<template>
  <div >
    <VueMarkdown class="markdown-body">
      {{ content }}
    </VueMarkdown>
  </div>
</template>

<script>
import VueMarkdown from "vue-markdown";

export default {
  name: "app",
  components: { VueMarkdown },
  data() {
    return {
      content: `
    
    当然可以,以下是一个简单的C++ HelloWorld程序:

\`\`\` c++
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
\`\`\` 
    `,
    };
  },
  methods: {
    change() {
      let t = {
        a: "111",
      };
      console.log("aaa", t);
      this.test = t;
    },
  },
};
</script>

<style>
@import 'github-markdown-css/github-markdown.css';
</style>
