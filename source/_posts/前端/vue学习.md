---
title: vue学习总结
date: 2023-4-1
---

# 前言

感觉vue好像有好多很好用的组件,我就来看看

# 基础



## 引用vue

```
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

## 模板语法

vue采用一种简洁的模板语法来绑定数据到 DOM。在 Vue 中，你可以在 HTML 模板中使用双大括号来插入文本，以及使用特殊的属性（称为指令）来实现数据绑定和其他功能。以下是 Vue 的一些主要模板语法特性：

1. 插值 (Interpolation)

   使用双大括号 将数据绑定到文本节点：

   ```
   <span>{{ message }\}</span>
   ```

2. 属性绑定 (Attribute Binding)

   使用 v-bind 指令绑定 HTML 属性：

   ```
   <img v-bind:src="imageSource" alt="Vue logo">
   <img :src="imageSource" alt="Vue logo">  简写方式
   ```

3. 条件渲染 (Conditional Rendering)

   使用 v-if、v-else-if 和 v-else 指令进行条件渲染：

   ```
   <div v-if="isVisible">显示内容</div>
   <div v-else-if="isError">错误信息</div>
   <div v-else>隐藏内容</div>
   ```

4. 循环渲染 (List Rendering)

   使用 v-for 指令渲染列表数据：

   ```
   <ul>
     <li v-for="item in items" :key="item.id">
       {{ item.text }}
     </li>
   </ul>
   ```

5. 事件监听 (Event Handling)

   使用 v-on 指令监听 DOM 事件：

   ```
   <button v-on:click="handleClick">点击我</button>
   <button @click="handleClick">点击我</button> 简写
   ```

6. 文本渲染 

   * v-text：用于更新元素的textContent
   * v-html：用于输出HTML字符串。(小心使用这个,可能会出现xss攻击)

7. v-cloak：解决在页面加载时出现的闪烁问题，可以在vue实例编译结束时，自动移除v-cloak属性。我们可以通过css和js对其进行一些操作,等到vue接管后移除这个属性

8. v-once：**只渲染元素和组件一次。随后的重新渲染, 元素/组件及其所有的子节点将被视为静态内容并跳过**。

9. v-pre  跳过模板编译,直接显示原始页面,可以减少一些渲染,比如我们一个容器里面不需要使用的指令的结点就可以不需要编译

10. 表单输入绑定 (Form Input Bindings)

   使用 v-model 指令实现双向数据绑定：

   ```
   <input v-model:value="message" placeholder="请输入内容">
   <input v-model="message" placeholder="请输入内容"> 简写
   ```

​		v-model 只能用于可以输入标签上

在表单字段,v-bind 是单向绑定, 只有当js数据发生变化的时候才会影响页面数据变化, 但是页面数据发生变化的时候,js变量数据不会发生变化,v-model是双向的

**模板中必须是在Vue对象身上有的变量才能使用**

**插值和指令里面要写js表达式**

## vue对象常用配置项

在创建一个 Vue 对象时，你需要向构造函数传递一个配置对象，其中包含一些属性和方法。以下是一些常用的配置项及其含义：

1. el: 指定 Vue 实例挂载到 DOM 的元素。可以是一个 CSS 选择器字符串，也可以是一个 HTML 元素。

   ```
   el: '#app'
   ```

2. data: 定义 Vue 实例的数据对象。这些数据会被 Vue 进行响应式处理，以便在数据变化时自动更新视图。

   ```
   // 对象式
   data: {
     message: 'Hello Vue!'
   }
   
   // 使用脚手架的时候必须使用这个方式,因为如果不使用这个方式的话,无法共享组件,数据会混乱
   // 函数式
   // 这里千万不能使用箭头函数
   data:function(){
   	return {
   		message:"Hello Vue!"
   	}
   }
   ```

3. methods: 定义 Vue 实例的方法。这些方法可以在模板中通过事件绑定或其他方式调用。

   ```
   methods: {
     handleClick: function () {
       alert('Button clicked!');
     }
   }
   ```

4. computed: 定义 Vue 实例的计算属性。计算属性是基于其他响应式数据进行计算的属性，会根据依赖数据的变化自动更新。

   ```
   computed: {
     reversedMessage: function () {
       return this.message.split('').reverse().join('');
     }
   }
   ```

5. watch: 定义 Vue 实例的监听器。监听器用于观察和响应数据的变化。

   ```
   watch: {
     message: function (newValue, oldValue) {
       console.log('新值:', newValue, '旧值:', oldValue);
     }
   }
   ```

6. components: 定义 Vue 实例的局部组件。这些组件只能在当前 Vue 实例的模板中使用。

   ```
   components: {
     'my-component': {
       template: '<div>自定义组件</div>'
     }
   }
   ```

7. props: 定义接收的属性，仅适用于 Vue 组件。

   ```
   props: ['title', 'content']
   ```

8. template: 定义组件的模板。可以是一个字符串模板，也可以是一个 HTML 元素。

   ```
   template: '<div>{{ message }}</div>'
   ```

9. mounted: 生命周期钩子，在 Vue 实例挂载到 DOM 之后调用。可以在这个钩子中执行一些初始化操作，如获取数据、添加事件监听器等。

   ```
   mounted: function () {
     console.log('Vue 实例已挂载');
   }
   ```

10. created: 生命周期钩子，在 Vue 实例创建完成后立即调用。此时，实例已完成以下配置：数据观测（data observer）、计算属性（computed properties）以及方法（methods）。

    ```
    created: function () {
      console.log('Vue 实例已创建');
    }
    ```

vue 在实例化过程中，会对这些配置项进行处理和初始化。以下是 Vue 对主要配置项所做的处理：

1. `data`：Vue 会将 `data` 中的属性添加到 Vue 实例上，并使这些属性变得响应式。这意味着当这些属性值发生变化时，Vue 会自动更新相关视图。Vue 还会将 `data` 属性代理到 Vue 实例本身，以便可以直接通过 `this.propertyName` 访问这些属性。
2. `computed`：Vue 会处理 `computed` 对象中定义的计算属性。计算属性是基于其他属性值（如 `data` 中的属性）计算得到的属性，它们会被缓存，只有当依赖的属性发生变化时，计算属性的值才会重新计算。
3. `watch`：Vue 会设置 `watch` 对象中定义的侦听器。侦听器允许你对 Vue 实例中的某个属性进行观察，当该属性的值发生变化时，侦听器会触发指定的回调函数。
4. `methods`：Vue 会将 `methods` 对象中定义的方法添加到 Vue 实例上，以便可以在 Vue 实例（如模板或其他方法）中使用这些方法。这些方法会自动绑定到 Vue 实例，因此可以在方法内部通过 `this` 访问 Vue 实例。
5. `el`：Vue 会将 `el` 选项作为挂载点，将 Vue 实例挂载到 DOM 元素上。你可以传递一个选择器字符串或一个 DOM 元素。Vue 会将编译好的模板替换这个元素。
6. `template`：Vue 会将 `template` 选项作为模板，用于渲染 Vue 实例。模板可以是一个字符串或一个 DOM 元素。在编译过程中，模板会被转换为虚拟 DOM，然后 Vue 会将虚拟 DOM 渲染为真实 DOM 并插入到页面中。
7. `components`：Vue 会注册 `components` 对象中定义的子组件。这些子组件可以在 Vue 实例的模板中使用，以便构建组件化的应用程序。
8. `props`：对于组件实例，Vue 会处理 `props` 对象中定义的属性。这些属性允许你从父组件向子组件传递数据。
9. `mixins`：Vue 会将 `mixins` 数组中的 mixin 对象合并到 Vue 实例的配置对象中。mixin 对象可以包含任意的 Vue 配置选项（如 `data`、`methods`、`computed` 等），这些选项将被合并到 Vue 实例中，实现代码复用

## MVVM模型

MVVM（Model-View-ViewModel）是一种软件架构设计模式，它将应用程序的逻辑、数据和界面分离。Vue.js 是一个基于 MVVM 模式的前端框架，它通过双向数据绑定在 Model（数据模型）和 View（视图）之间建立联系，而 ViewModel（视图模型）充当这两者之间的桥梁。

在 Vue 中，MVVM 的组成部分如下：

1. Model（数据模型）：在 Vue 中，Model 通常是一个 JavaScript 对象，它包含应用程序的数据和业务逻辑。Model 位于 Vue 实例的 data 属性中，是响应式的，即当数据发生变化时，Vue 会自动更新与之相关的视图。
2. View（视图）：视图是指用户界面，即 HTML 模板。在 Vue 中，视图使用模板语法与 Model 进行绑定，包括插值、属性绑定、事件监听等。当 Model 中的数据发生变化时，视图会自动更新。
3. ViewModel（视图模型）：ViewModel 是 Vue 实例本身，它充当 Model 和 View 之间的桥梁。ViewModel 监听 Model 中数据的变化，并通过双向数据绑定自动更新视图。同时，它还处理用户在视图中触发的事件，如按钮点击、表单提交等，并根据需要更新 Model。

Vue.js 的 MVVM 模式实现了 Model 和 View 之间的解耦，使得开发者可以专注于业务逻辑，而无需关心 DOM 操作和事件处理。这样可以提高代码的可维护性、可复用性和可测试性。

## 数据代理

在 Vue.js 中，**数据代理指的是 Vue 实例可以直接访问其 data 对象中的属性，而无需通过 data 对象本身**。这意味着你可以使用 `this.propertyName` 访问和操作 data 中的属性，而不是 `this.data.propertyName`。**数据代理简化了代码并提高了可读性**。

数据代理的原理是基于 JavaScript 的访问器属性（getter 和 setter）和 `Object.defineProperty` 方法实现的。Vue 在创建实例时，会遍历 data 对象的属性，并通过 `Object.defineProperty` 为每个属性定义 getter 和 setter。这样，当你访问或修改 Vue 实例上的属性时，实际上是通过代理访问或修改 data 对象中的对应属性。

以下是一个简化的数据代理实现示例：

```
function Vue(options) {
  this.data = options.data;
  this.proxyData();
}

Vue.prototype.proxyData = function () {
  for (const key in this.data) {
    if (this.data.hasOwnProperty(key)) {
      Object.defineProperty(this, key, {
        enumerable: true,
        configurable: true,
        get: () => {
          return this.data[key];
        },
        set: (newValue) => {
          this.data[key] = newValue;
        },
      });
    }
  }
};
```

## 数据劫持

vue.js 中的数据劫持是指框架通过劫持对象属性的 getter 和 setter 方法，以实现对数据的监听和响应式更新。当数据发生变化时，Vue.js 能够自动检测到这些变化，**并更新相关的视图**。数据劫持是 Vue.js 实现双向数据绑定和响应式更新的核心技术。

Vue.js 中的数据劫持主要是通过 `Object.defineProperty` 方法实现的。具体实现过程如下：

1. 遍历 data 对象的属性：在创建 Vue 实例时，框架会遍历 data 对象的所有属性。
2. 为每个属性定义 getter 和 setter：使用 `Object.defineProperty` 方法为每个属性定义访问器属性，即 getter 和 setter 方法。
3. 在 getter 中收集依赖：当访问某个属性时，getter 方法会被触发。在 getter 中，Vue.js 会收集当前属性的依赖（如计算属性、模板等）。
4. 在 setter 中触发更新：当修改某个属性时，setter 方法会被触发。在 setter 中，Vue.js 会通知与该属性相关的依赖进行更新，从而实现响应式更新。

以下是一个简化的数据劫持实现示例：

```
function observe(data) {
  if (!data || typeof data !== 'object') {
    return;
  }

  for (const key in data) {
    if (data.hasOwnProperty(key)) {
      let value = data[key];
      observe(value); // 递归处理嵌套对象

      Object.defineProperty(data, key, {
        enumerable: true,
        configurable: true,
        get: () => {
          console.log('访问:', key, value);
          return value;
        },
        set: (newValue) => {
          console.log('修改:', key, newValue);
          if (newValue !== value) {
            value = newValue;
            observe(newValue); // 如果设置了新的对象，则继续劫持新对象的属性
          }
        },
      });
    }
  }
}
```

这里利用了闭包能够保存临时变量的特点

### 劫持数据类型的区别

1. **对象**：对于对象，Vue 会遍历对象的所有属性，使用 Object.defineProperty（Vue 2.x）或 Proxy（Vue 3.x）对每个属性进行劫持。当属性值发生变化时，Vue 会被通知并触发视图更新。这种方法适用于对象，因为它可以精确地监视每个属性的变化。
2. **数组**：对于数组，Vue 会使用不同的策略进行数据劫持。使用 Object.defineProperty 或 Proxy 对数组的索引进行劫持并不是一个好主意，因为这样会导致性能问题。相反，Vue 使用一种基于原型链的方法来监视数组变化。Vue 会覆盖数组的一些原生方法，如 `push`、`pop`、`shift`、`unshift`、`splice`、`sort` 和 `reverse`。当这些方法被调用时，Vue 会执行原生操作，并同时通知视图更新。这样可以避免对数组索引进行劫持，从而提高性能。

如果我们的数组里面包含了对象比如这样

```
persons: [{ id: 1, age: 25, name: '张三' }]
```

persons[0].age = 30   这种方式可以检测到

persons[0] = { id: 1, age: 30, name: '张三' }  这种方式检测不到,因此不会更新视图

### 后期添加数据劫持

在 Vue 中，如果要在实例创建之后添加新的响应式属性，你不能直接将新属性添加到对象或数组中，因为 Vue 默认情况下无法检测到这种变化。相反，你需要使用 Vue 提供的特殊方法：`Vue.set()`（或 `this.$set()`）和 `Vue.delete()`（或 `this.$delete()`）。

以下是如何使用这些方法在 Vue 实例中添加和删除响应式属性的示例：

1. **为对象添加响应式属性**：

```
// 在 Vue 实例中添加一个新的响应式属性 `newProperty`
this.$set(this.someObject, 'newProperty', 'New Value');
```

1. **为数组添加响应式元素**：

```
// 向 Vue 实例中的数组添加一个新的响应式元素
this.$set(this.someArray, index, newValue);
```

需要注意的是，如果你要添加的属性本身是一个对象或数组，这个对象或数组中的值也将变成响应式的。

总之，在 Vue 实例创建之后，如果需要添加新的响应式属性，请使用 `Vue.set()`（或 `this.$set()`）方法。这将确保新属性是响应式的，并且在属性值发生变化时能够触发视图更新。

> 这个不能应用到vue._data 和 vue身上

## 收集表单数据

`v-model` 在表单输入框中绑定的值对应于 Vue 实例中的数据属性。当你在输入框中输入内容时，`v-model` 会自动将输入的值与 Vue 实例中的相应数据属性保持同步。这样，你可以轻松地访问和处理用户输入的数据。

以下是使用 `v-model` 在不同类型的表单元素中绑定的数据含义：

1. **文本输入框（`<input type="text">`）**：`v-model` 会绑定输入框中的文本值。当用户输入内容时，**输入框的值**将实时同步到 Vue 实例的相应数据属性。
2. **数值输入框（`<input type="number">`）**：`v-model` 会绑定输入框中的数值。与文本输入框类似，输入的数值会实时同步到 Vue 实例的相应数据属性。
3. **单选框（`<input type="radio">`）**：`v-model` 会绑定被选中的单选框的值。当用户选择一个单选框时，选中的值将同步到 Vue 实例的相应数据属性。
4. **复选框（`<input type="checkbox">`）**：**初始值会影响,如果是一个数据,代表是多个复选框,其他就是单个复选框**
   - 单个复选框：`v-model` 会绑定一个布尔值，表示复选框是否被选中。当用户选中或取消选中复选框时，布尔值将同步到 Vue 实例的相应数据属性。
   - 多个复选框：**`v-model` 会绑定一个数组**，其中包含所有被选中复选框的值。当用户选中或取消选中复选框时，数组将实时更新以反映当前选中的值。
5. **下拉列表（`<select>`）**：
   - 单选下拉列表：`v-model` 会绑定选中的选项的值。当用户选择一个选项时，选中的值将同步到 Vue 实例的相应数据属性。
   - 多选下拉列表：`v-model` 会绑定一个数组，其中包含所有被选中选项的值。当用户选中或取消选中选项时，数组将实时更新以反映当前选中的值。

这就是使用 `v-model` 在各种类型的表单输入框中绑定的数据含义。这些数据将实时同步到 Vue 实例中的相应数据属性，使得处理和验证用户输入变得更加简单。

### v-model的修饰符

1. **`.lazy`**：默认情况下，`v-model` 在输入框的 `input` 事件上进行同步。使用 `.lazy` 修饰符会将同步行为更改为在输入框的 `change` 事件上进行。这样，输入框的值只有在失去焦点时才会同步到 Vue 实例的数据属性。

   示例：

   ```
   <input v-model.lazy="message" />
   ```

2. **`.number`**：使用 `.number` 修饰符会将用户输入的值自动转换为 Number 类型。如果输入值无法被转换为有效的数字，结果将为 NaN。这在需要确保输入值为数字类型时非常有用。

   示例：

   ```
   <input v-model.number="age" type="text" />
   ```

3. **`.trim`**：`.trim` 修饰符用于自动去除用户输入的首尾空白字符。当输入框的值同步到 Vue 实例的数据属性时，首尾空白字符将被删除。

   示例：

   ```
   <input v-model.trim="message" />
   ```

## 事件绑定

在 Vue.js 中，使用 `v-on` 指令来绑定事件监听器。通过 `v-on`，你可以在 DOM 元素上绑定事件，例如点击、双击、键盘事件等，并调用 Vue 实例中的方法来处理这些事件。你还可以设置一些修饰符和传递参数来定制事件处理

以下是 `v-on` 的一些使用方法和设置:

### 绑定事件

使用 `v-on:eventName` 语法来绑定事件。将 `eventName` 替换为要监听的事件名称，例如 `click`、`dblclick`、`keydown` 等。

```
<button v-on:click="handleClick">点击我</button>
```

### 调用方法

在 Vue 实例的 `methods` 属性中定义事件处理方法，然后在 `v-on` 指令中指定该方法。

```
<script>
  new Vue({
    el: '#app',
    methods: {
      handleClick: function() {
        alert('按钮被点击了！');
      }
    }
  });
</script>
```

使用简写语法：`v-on` 支持简写语法 `@`。例如，可以使用 `@click` 代替 `v-on:click`。

```
<button @click="handleClick">点击我</button>
```

### **传递参数**

在事件处理方法中，可以接收事件对象作为参数。还可以在绑定事件时传递自定义参数。

```
<button @click="handleClick($event, '自定义参数')">点击我</button>

<script>
  new Vue({
    el: '#app',
    methods: {
      handleClick: function(event, customParam) {
        console.log(event, customParam);
      }
    }
  });
</script>
```

### **事件修饰符**

Vue.js 提供了一些事件修饰符，用于处理事件细节。事件修饰符以点 `.` 开头，跟在事件名称后面。

- `.stop`：阻止事件冒泡。(常用)
- `.prevent`：阻止事件的默认行为。(常用)
- `.once`：只触发一次事件处理函数。(常用)
- `.capture`：使用事件捕获模式而不是冒泡模式。
- `.self`：只在事件在当前元素（而非子元素）上触发时调用处理函数。
- `.passive`：以被动模式添加事件监听器。比如滚轮事件, 滚动之后我们需要去远程下载一张图片,如果不使用这个修饰符,滚动条得等到图片下载完毕才能滚动, 如果使用这个修饰符,不用等图片下载完毕就能滚动

```
<!-- 阻止事件冒泡 -->
<button @click.stop="handleClick">点击我</button>

<!-- 阻止事件默认行为 -->
<a @click.prevent="handleClick" href="https://example.com">点击我</a>

<!-- 使用事件捕获模式 -->
<button @click.capture="handleClick">点击我</button>

<!-- 只在当前元素触发事件 -->
<button @click.self="handleClick">点击我</button>

<!-- 只触发一次事件处理函数 -->
<button @click.once="handleClick">点击我</button>

<!-- 以被动模式添加事件监听器 -->
<button @click.passive="handleClick">点击我</button>
```

### **按键修饰符**

对于对于键盘事件，Vue.js 提供了按键修饰符来监听特定按键的事件。按键修饰符同样以点 `.` 开头，跟在事件名称后面。

以下是一些常见的按键修饰符：

- `.enter`
- `.tab`
- `.delete` (捕获 "删除" 和 "退格" 键)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`

例如，你可以在 `keydown` 事件中使用按键修饰符来监听 Enter 键：

```
<input @keydown.enter="handleEnter" />

<script>
  new Vue({
    el: '#app',
    methods: {
      handleEnter: function() {
        console.log('按下了 Enter 键');
      }
    }
  });
</script>
```

你还可以自定义按键别名。在 Vue 实例的全局配置中，使用 `Vue.config.keyCodes` 对象添加自定义按键别名：

```
Vue.config.keyCodes.customKey = 123; // 将按键码 123 映射为 "customKey"

// 然后在模板中使用自定义按键修饰符
// <input @keydown.customKey="handleCustomKey" />
```

总结一下，Vue.js 中的事件绑定可以通过 `v-on` 指令实现，支持多种设置选项，如传递参数、使用事件修饰符和按键修饰符等。这些设置选项可以帮助你方便地处理不同场景下的事件监听和处理。

## 计算属性

Vue.js 中的计算属性（Computed properties）是一种特殊类型的属性，它们的值是通过其他属性（通常是 `data` 中的属性）进行计算得到的。计算属性在 Vue 实例的 `computed` 选项中定义。与普通属性不同，计算属性会被缓存，**只有当依赖的属性(Vue劫持了的数据)发生变化时**，计算属性的值才会重新计算。这有助于提高性能，特别是当计算过程复杂或计算代价较高时

计算属性主要包含两个配置项：`get` 和 `set`。

`get`：用于计算属性的计算函数。当访问计算属性时，`get` 函数将被调用，用于计算属性的值。通常，`get` 函数会根据其他属性（如 `data` 中的属性）的值来计算结果。默认情况下，如果你直接在 `computed` 对象中定义一个函数，那么它就是 `get` 函数。

```
javascriptCopy codecomputed: {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
```

set`：用于设置计算属性的函数。当尝试修改计算属性的值时，`set` 函数将被调用。通常，`set` 函数会根据传入的新值来更新其他相关属性（如 `data` 中的属性）。

```
javascriptCopy codecomputed: {
  fullName: {
    get: function() {
      return this.firstName + " " + this.lastName;
    },
    set: function(newValue) {
      var names = newValue.split(" ");
      this.firstName = names[0];
      this.lastName = names[1];
    }
  }
}
```

在这个例子中，我们定义了一个名为 `fullName` 的计算属性，它具有 `get` 和 `set` 函数。当访问 `fullName` 时，`get` 函数将根据 `firstName` 和 `lastName` 属性计算结果。当尝试修改 `fullName` 的值时，`set` 函数将被调用，并根据新值更新 `firstName` 和 `lastName` 属性。

总之，计算属性的主要配置项包括 `get` 和 `set` 函数。`get` 函数用于计算属性的值，而 `set` 函数用于设置计算属性的值。通过这两个函数，你可以方便地处理基于其他属性的计算和更新逻辑。

### 计算属性的优势

1. **缓存**：计算属性会缓存计算结果。只有当依赖的属性发生变化时，计算属性才会重新计算。这有助于提高性能，特别是当计算过程复杂或计算代价较高时。
2. **响应式**：计算属性依赖于其他响应式属性。当依赖的属性发生变化时，计算属性会自动更新。这使得计算属性在处理复杂逻辑和依赖关系时非常方便。
3. **可读性**：计算属性可以将复杂的逻辑封装在一个属性中，提高代码的可读性和可维护性。

### 计算属性与方法的区别

尽管你也可以在 Vue 实例的 `methods` 选项中定义方法来实现类似的功能，但计算属性具有缓存和响应式的优势。当多次访问同一个计算属性时，计算属性会返回缓存的结果，而不是重新计算。相反，使用方法时，**每次调用方法**都会重新计算结果。因此，在性能和依赖处理方面，计算属性更具优势。

## 监视属性

监视属性（Watch properties）是 Vue 中用于观察和响应 Vue 实例上属性值变化的一种机制。**它允许你为某个属性指定一个回调函数**，当该属性的值发生变化时，回调函数将被调用。你可以在 Vue 实例的 `watch` 选项中定义监视属性。

以下是 `watch` 选项的一些配置：

**普通监视函数**：为要监视的属性提供一个回调函数。回调函数接收两个参数：新值（`newVal`）和旧值（`oldVal`）。

```
watch: {
  propertyName: function(newVal, oldVal) {
    // 在这里执行属性值变化时的操作
  }
}
```

**立即执行的监视函数**：如果你希望监视函数在 Vue 实例初始化时立即执行，可以使用 `handler` 属性定义回调函数，并将 `immediate` 属性设置为 `true`。

```
watch: {
  propertyName: {
    handler: function(newVal, oldVal) {
      // 在这里执行属性值变化时的操作
    },
    immediate: true
  }
}
```

**带延迟的监视函数**：如果你希望在属性值发生变化后延迟一段时间再执行回调函数，可以使用 `handler` 属性定义回调函数，并设置 `delay` 属性为一个毫秒值。

```
watch: {
  propertyName: {
    handler: function(newVal, oldVal) {
      // 在这里执行属性值变化时的操作
    },
    delay: 500 // 延迟 500 毫秒后执行回调函数
  }
}
```

**深度监视**：默认情况下，Vue 只监视属性的一级变化。如果你需要监视一个对象的嵌套属性，可以将 `deep` 属性设置为 `true`。

```
watch: {
  objectProperty: {
    handler: function(newVal, oldVal) {
      // 在这里执行属性值变化时的操作
    },
    deep: true // 深度监视嵌套属性变化
  }
}
```

> 除了使用new Vue的时候传入监视配置,也可以在后面使用 Vue的$watch方法
>
> 如果是多层结构的话  监视名字得这样  "a.b.c"

监视属性的主要用途是在属性值发生变化时执行某些操作，例如数据验证、数据获取、状态更新等。监视属性特别适用于处理异步或昂贵操作的情况。

**监视属性能够监视  vue自己通过Object.defineProperty方法往自己身上加的属性 比如 data里面的数据  计算属性**

值得注意的是，监视属性并非适用于所有情况。在很多情况下，计算属性可能是更好的选择，特别是当你需要根据其他属性计算一个值时。然而，监视属性在处理异步操作和昂贵操作时非常有用，因为它们允许你在属性值发生变化时执行特定操作。



## Class 与 Style 绑定

### class 绑定



在 Vue 中，你可以使用 `v-bind:class`（简写为 `:class`）动态地绑定 class。以下是一些常见的 class 绑定规则以及它们的使用方法：

**字符串语法**：直接将字符串作为 class 名传递给 `v-bind:class`。字符串中的类名将被添加到元素上。

```
<div v-bind:class="className"></div>
```

在这个例子中，`className` 可以是一个字符串，也可以是返回字符串的计算属性。

**对象语法**：使用对象语法，你可以根据对象的属性值（布尔值）动态地切换类。对象的属性名表示要绑定的类名，属性值为布尔值，决定是否应用该类。

```
<div v-bind:class="{ active: isActive, error: hasError }"></div>
```

在这个例子中，`active` 类将只在 `isActive` 为 `true` 时应用；`error` 类将只在 `hasError` 为 `true` 时应用。

**数组语法**：使用数组语法，你可以将一个包含类名的数组传递给 `v-bind:class`。数组中的所有类名将被添加到元素上。

```
<div v-bind:class="[classA, classB]"></div>
```

在这个例子中，`classA` 和 `classB` 都会被添加到元素上。它们可以是字符串或计算属性。

**数组语法中的对象**：在数组语法中，你还可以使用对象来根据条件切换类名。

```
<div v-bind:class="[{ active: isActive }, classB]"></div>
```

在这个例子中，`active` 类将只在 `isActive` 为 `true` 时应用；`classB` 总是会被添加到元素上。

**绑定组件的 class**：在自定义组件中，你可以使用 `v-bind:class` 来绑定类。这些类将被添加到组件的根元素上。

```
<my-component v-bind:class="{ active: isActive }"></my-component>
```

在这个例子中，如果 `isActive` 为 `true`，则 `active` 类将被添加到 `my-component` 的根元素上。

### style绑定

在 Vue 中，你可以使用 `v-bind:style`（简写为 `:style`）动态地绑定 style。以下是一些常见的 style 绑定规则以及它们的使用方法：

**对象语法**：使用对象语法，你可以将一个包含 CSS 属性及其值的对象传递给 `v-bind:style`。对象的属性名应为驼峰式（camelCase）或短横线分隔（kebab-case，需要加引号）的 CSS 属性名，属性值为相应的样式值。

```
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

在这个例子中，`activeColor` 和 `fontSize` 可以是 data 属性、计算属性或方法的返回值。

**数组语法**：使用数组语法，你可以将一个包含多个样式对象的数组传递给 `v-bind:style`。数组中的所有样式对象将被合并，并应用到元素上。

```
<div v-bind:style="[styleObjectA, styleObjectB]"></div>
```

在这个例子中，`styleObjectA` 和 `styleObjectB` 都应该是包含样式属性及其值的对象。它们可以是 data 属性、计算属性或方法的返回值。

**自动添加前缀**：Vue 会自动为某些需要浏览器前缀的 CSS 属性添加前缀，如 `transform`。你只需要写标准的 CSS 属性名，Vue 会自动处理浏览器兼容性问题。**绑定组件的 style**：在自定义组件中，你可以使用 `v-bind:style` 来绑定样式。这些样式将被添加到组件的根元素上。

```
<my-component v-bind:style="{ color: activeColor }"></my-component>
```

在这个例子中，`activeColor` 的值将被应用到 `my-component` 的根元素上。

> 我们绑定的class和style都是追加到标签的属性中的, 也就是说我们固定的属性并不会被删掉

## 条件渲染

ue 提供了一些指令来实现条件渲染。这些指令可以根据表达式的值动态地添加或删除元素。以下是 Vue 中常见的条件渲染指令：

**v-if**：`v-if` 指令用于根据一个表达式的真假值来决定是否渲染一个元素。如果表达式的值为真（truthy），则该元素将被渲染；否则，该元素将不会被渲染。

```
<div v-if="show">这个元素将根据 show 的值进行条件渲染。</div>
```

在这个例子中，如果 `show` 的值为真（truthy），则该元素将被渲染；否则，不会被渲染。

**v-else**：`v-else` 指令用于表示一个与 `v-if` 配套使用的“否则”分支。`v-else` 必须紧跟在一个带有 `v-if` 的元素之后，它们共同表示一个条件渲染的 if-else 结构。

```
<div v-if="show">这个元素将在 show 为真时渲染。</div>
<div v-else>这个元素将在 show 为假时渲染。</div>
```

在这个例子中，当 `show` 的值为真时，第一个元素将被渲染；否则，第二个元素将被渲染。

**v-else-if**：`v-else-if` 指令用于表示一个与 `v-if` 配套使用的“否则如果”分支。`v-else-if` 必须紧跟在一个带有 `v-if` 或 `v-else-if` 的元素之后，它们共同表示一个条件渲染的 if-elseif-else 结构。

```
<div v-if="type === 'A'">这个元素将在 type 为 'A' 时渲染。</div>
<div v-else-if="type === 'B'">这个元素将在 type 为 'B' 时渲染。</div>
<div v-else>这个元素将在 type 不是 'A' 或 'B' 时渲染。</div>
```

在这个例子中，根据 `type` 的值，将渲染不同的元素。

**v-show**：`v-show` 指令与 `v-if` 类似，也用于根据一个表达式的真假值来决定是否显示一个元素。但与 `v-if` 不同的是，`v-show` 不会实际移除或添加元素，而是通过 CSS 的 `display` 属性来控制元素的显示和隐藏。

```
htmlCopy code
<div v-show="show">这个元素将根据 show 的值进行显示或隐藏。</div>
```

在这个例子中，如果 `show` 的值为真,则该元素将被显示；否则，该元素将被隐藏。请注意，`v-show` 只是简单地切换元素的 CSS `display` 属性，而不是像 `v-if` 那样实际移除或添加元素。

**v-if 与 v-show 的区别**

尽管 `v-if` 和 `v-show` 都可以实现条件渲染，但它们在某些方面有所不同：

- `v-if` 是真正的条件渲染，它会在条件满足时将元素添加到 DOM，条件不满足时将元素从 DOM 移除。这意味着切换 `v-if` 的条件会触发组件的销毁与重建，以及过渡效果。
- `v-show` 只是简单地切换元素的 CSS `display` 属性。无论条件是否满足，元素始终存在于 DOM 中，只是显示或隐藏。这意味着 `v-show` 的切换不会触发组件的销毁与重建，以及过渡效果。

在选择 `v-if` 和 `v-show` 时，可以根据以下原则来决定：

- 如果需要频繁切换显示和隐藏的元素，使用 `v-show` 可能更合适，因为它不会导致组件的销毁与重建，性能较好。
- 如果元素可能永远不会被显示，或者条件改变较少的情况下，使用 `v-if` 更合适，因为它可以减少初始渲染的开销。

## 列表渲染

在 Vue 中，列表渲染是一种常见的需求。为了方便地渲染列表数据，Vue 提供了 `v-for` 指令。`v-for` 可以遍历数组或对象，并为每个元素生成一个模板实例。

以下是关于 Vue 中列表渲染的一些用法：

**遍历数组**：使用 `v-for` 遍历数组时，需要提供一个表达式，表示“元素 in 数组”。遍历过程中，每个元素都将被绑定到当前模板实例。

```
<ul>
  <li v-for="item in items">{{ item }}</li>
</ul>
```

在这个例子中，`items` 是一个数组，`item` 是数组中的每个元素。`v-for` 将为 `items` 中的每个元素生成一个 `<li>` 标签。

**遍历对象**：使用 `v-for` 遍历对象时，需要提供一个表达式，表示“(值, 键) in 对象”。遍历过程中，对象的每个属性都将被绑定到当前模板实例。

```
<ul>
  <li v-for="(value, key) in object">{{ key }}: {{ value }}</li>
</ul>
```

在这个例子中，`object` 是一个对象，`key` 是对象中的每个属性名，`value` 是对象中每个属性的值。`v-for` 将为 `object` 中的每个属性生成一个 `<li>` 标签。

**遍历指定次数**: 我们可以指定次数遍历

```
<p v-for="(n,i) in 5">{{i}}-{{n}}</p>
```

索引从0开始,数字从1开始

**遍历数组或对象时获取索引**：在遍历数组或对象时，你可以使用第三个参数获取当前元素的索引。

```
<!-- 遍历数组时获取索引 -->
<ul>
  <li v-for="(item, index) in items">{{ index }}: {{ item }}</li>
</ul>

<!-- 遍历对象时获取索引 -->
<ul>
  <li v-for="(value, key, index) in object">{{ index }} - {{ key }}: {{ value }}</li>
</ul>
```

**在组件上使用 `v-for`**：在自定义组件中，你可以使用 `v-for` 来遍历数据。遍历过程中，每个元素都将作为 prop 传递给组件。

```
<my-component v-for="item in items" v-bind:item="item" v-bind:key="item.id"></my-component>
```

在这个例子中，`items` 是一个数组，`item` 是数组中的每个元素。`v-for` 将为 `items` 中的每个元素生成一个 `my-component` 组件实例。请注意，为了提高性能和避免重复渲染，你应该使用 `v-bind:key` 为每个组件实例绑定一个唯一的键值（通常是数据的 ID）。



在 Vue 中的列表渲染中，`key` 属性是一个特殊的属性，用于跟踪每个节点的唯一性。**当 Vue 更新 DOM 时，它会尽可能地复用和重排现有的元素，而不是从头开始渲染。通过为每个列表项提供一个唯一的 `key`，可以帮助 Vue 更高效地识别和管理这些节点**。

以下是关于 `key` 属性的一些特点和好处：

1. **提高性能**：`key` 的主要作用是提高列表渲染的性能。当列表发生变化时（例如，添加、删除、重新排序等操作），Vue 会根据每个节点的 `key` 来判断是否可以复用现有的 DOM 元素。这可以避免不必要的渲染，从而提高性能。
2. **维护组件状态**：当你在列表中使用组件时，使用 `key` 可以帮助 Vue 维护组件的状态。在某些情况下，如果没有使用 `key`，当列表发生变化时，Vue 可能会复用组件实例，这可能导致组件状态出现问题。通过为每个组件实例提供一个唯一的 `key`，可以确保 Vue 正确地追踪和管理组件状态。
3. **唯一且稳定**：`key` 的值应该是唯一且稳定的，这样 Vue 才能正确地追踪节点。通常情况下，你可以使用数据项的唯一 ID 作为 `key`。在某些特殊情况下，你也可以使用其他唯一且稳定的值，例如索引（但这可能会导致性能和状态管理问题，因此不推荐）。

以下是一个使用 `key` 的列表渲染示例：

```
<ul>
  <li v-for="item in items" v-bind:key="item.id">{{ item.text }}</li>
</ul>
```

在这个例子中，`items` 是一个数组，每个元素都包含一个唯一的 `id`。`v-for` 为 `items` 中的每个元素生成一个 `<li>` 标签，并使用 `v-bind:key` 为每个标签绑定一个唯一的 `key`。

`key` 属性如何帮助 Vue 复用现有的 DOM 元素主要是通过 Vue 的 diff 算法实现的。当列表数据发生变化时，Vue 会通过这个算法比较**新旧虚拟 DOM 树**，以确定是否可以复用现有的 DOM 元素。`key` 在这个过程中起到了关键作用，它可以帮助 Vue 更准确地识别哪些节点可以被复用。

以下是关于 `key` 如何帮助复用 DOM 元素的简要说明：

1. **创建虚拟 DOM 树**：当 Vue 组件渲染时，它会创建一个虚拟 DOM 树来表示真实的 DOM 结构。虚拟 DOM 树是一个轻量级的 JavaScript 对象，它包含了节点的类型、属性、事件等信息。`key` 属性也会被包含在虚拟 DOM 节点中。
2. **比较新旧虚拟 DOM 树**：当组件状态发生变化时，Vue 会创建一个新的虚拟 DOM 树，并将其与旧的虚拟 DOM 树进行比较。这个比较过程称为 diff 算法。
3. **识别可复用节点**：在 diff 算法过程中，Vue 会尝试找到可以复用的节点。为了找到这些节点，Vue 需要确定新旧虚拟 DOM 树中的节点是否相同。**`key` 在这个过程中起到了重要作用。当两个节点具有相同的 `key` 时，Vue 认为它们是相同的**，因此可以尝试**复用现有的相同的 DOM** 元素。如果没有 `key` 或 `key` 不同，Vue 将创建一个新的 DOM 元素。
4. **更新 DOM**：根据 diff 算法的结果，Vue 会对真实的 DOM 进行更新。对于可以复用的节点，Vue 会更新其属性、事件等，而不是重新创建。这样可以避免不必要的渲染开销，提高性能。

总之，`key` 在 Vue 的列表渲染中扮演着重要的角色，它可以提高性能、确保正确的组件状态管理，以及帮助 Vue 更高效地追踪和管理节点。因此，在使用 `v-for` 进行列表渲染时，建议总是为每个节点提供一个唯一的 `key`。

## 过滤器

Vue.js 中的过滤器（filters）是一种特殊的函数，用于对数据进行格式化或转换。过滤器通常与插值表达式和 `v-bind` 指令一起使用，使得在模板中对数据进行格式化变得简单。

过滤器的主要用途是处理一些简单的文本格式化，如大小写转换、货币格式化、日期格式化等。它们不会改变原始数据，只是对数据进行转换后显示。

要在 Vue.js 中使用过滤器，需要遵循以下步骤：

1. **定义过滤器**：在 Vue 实例的 `filters` 选项中定义过滤器函数。**过滤器函数始终接收原始值作为第一个参数**，可以接受额外的参数,在使用的的时候直接函数式传参就行  。

   示例：

   ```
   filters: {
     repeatString(value, count, separator) {
       if (!value) return '';
       value = value.toString();
       return Array(count).fill(value).join(separator);
     }
   }
   
   ```

2. **使用过滤器**：在插值表达式或 `v-bind` 指令中，使用管道符（`|`）将原始值传递给过滤器函数。

   示例：

   ```
   <!-- 在插值表达式中使用过滤器 -->
   <p>{{ message | repeatString(3, ', ') }}</p>
   
   
   <!-- 在 v-bind 指令中使用过滤器 -->
   <p v-bind:title="message | repeatString(3, ', ')">Hover to see  title</p>
   ```

你还可以将多个过滤器链式使用，将一个过滤器的输出作为另一个过滤器的输入。只需用管道符（`|`）分隔过滤器名称即可。

示例：

```
htmlCopy code<!-- 链式使用过滤器 -->
<p>{{ message | repeatString(3, ', ') | reverse }}</p>
```

需要注意的是，Vue.js 过滤器的主要目的是处理简单的文本格式化，而不是用于处理复杂数值计算或逻辑。对于复杂数值计算或逻辑，建议使用计算属性或方法。

### 全局过滤器

在配置项里面写好的是局部过滤器,只能在局部使用,全局过滤器可以在任何 Vue 实例或组件中使用，而无需在每个实例中单独定义

以下是一个创建全局过滤器的示例：

1. **定义全局过滤器**：在创建 Vue 实例之前，使用 `Vue.filter()` 方法定义全局过滤器。该方法接受两个参数：过滤器名称（字符串）和过滤器函数。

```
Vue.filter('capitalize', function (value) {
  if (!value) return '';
  value = value.toString();
  return value.charAt(0).toUpperCase() + value.slice(1);
});
```

2. **使用全局过滤器**：在任何 Vue 实例或组件的插值表达式或 `v-bind` 指令中，使用管道符（`|`）将原始值传递给全局过滤器。

```
<!-- 在插值表达式中使用全局过滤器 -->
<p>{{ message | capitalize }}</p>

<!-- 在 v-bind 指令中使用全局过滤器 -->
<p v-bind:title="message | capitalize">Hover to see capitalized title</p>
```

全局过滤器在整个应用程序中都可以使用，这意味着你只需要在一个地方定义过滤器，就可以在多个 Vue 实例或组件中使用它。但请注意，**如果全局过滤器与局部过滤器同名，局部过滤器将优先使用**。

> 过滤器只支持插值语法跟 v-bind

## 自定义指令

在Vue中，自定义指令允许你为元素添加特定的行为，有时候这比组件更加方便。自定义指令可以帮助你封装和重用一些DOM操作逻辑，使代码更易于阅读和维护。

以下是如何创建和使用自定义指令的详细步骤：

**注册全局自定义指令**：

```
Vue.directive('focus', {
  inserted: function (el) {
    el.focus()
  }
})
```

**注册局部自定义指令**：

```
new Vue({
  el: '#app',
  directives: {
    focus: {  // 这个就是指令名字,但是使用的时候得用v-开头
      inserted: function (el) {
        el.focus()
      }
    }
  }
})
```

**在模板中使用自定义指令**：

```
<input v-focus>  // 注意使用 v-  +  指令名字
```

自定义指令的配置项：

- bind：指令第一次绑定到元素时调用，可以进行一次性的初始化设置。
- inserted：被绑定元素插入父节点时调用（仅需父节点存在，不必存在于document中）。
- update：所在组件的 VNode 更新时调用，可能在其子 VNode 更新之前。指令的值可能发生了改变，也可能没有。
- componentUpdated：指令所在组件的 VNode 及其子 VNode 全部更新后调用。
- unbind：指令与元素解绑时调用，可以进行一些清理工作。

> 如果是函数式的话,在bind和update会执行这个函数

钩子函数的参数：

- el：指令所绑定的元素，可用于直接操作DOM。
- binding：包含以下属性的对象：
  - **name**：指令名，不包括v-前缀。
  - **value**：指令的绑定值。例如：`v-focus="1 + 1"`中，绑定值为`2`。
  - oldValue：指令绑定的前一个值，仅在update和component Updated钩子中可用。
  - expression：字符串形式的指令表达式。例如：`v-focus="1 + 1"`中，表达式为`"1 + 1"`。
  - arg：传给指令的参数。例如：`v-focus:arg`中，arg为参数。
  - **modifiers**：**一个包含修饰符的对象**。例如：`v-focus.foo.bar`中，修饰符对象为`{ foo: true, bar: true }`。
- vnode：Vue编译生成的虚拟节点。
- oldVnode：上一个虚拟节点，仅在update和componentUpdated钩子中可用。

使用自定义指令时需要注意：

1. 不要在自定义指令中修改数据，尽量仅用于操作DOM。因为它并不具备响应式机制，可能导致数据和视图不一致。
2. 在编写自定义指令时，遵循Vue的单向数据流原则，尽量避免双向绑定。如果需要实现类似于双向绑定的功能，可以考虑使用组件或通过事件通信实现。
3. 避免在自定义指令中执行耗时操作，因为这可能导致界面卡顿或性能下降。对于复杂的操作，可以考虑使用计算属性、侦听器或生命周期钩子。
4. 注意指令的作用域。全局指令在整个应用中都可以使用，而局部指令仅在指定的Vue实例或组件中可用。如果指令具有通用性，可以注册为全局指令；如果仅在特定组件中使用，可以注册为局部指令。
5. 使用修饰符来扩展指令的功能。修饰符是以`.`分隔的特殊后缀，可以用于指示指令应以某种特定方式绑定。例如，你可以使用修饰符来表示在更新DOM时是否使用动画效果。
6. 注意自定义指令与Vue内置指令的命名冲突。避免使用与内置指令相同或相似的名称，以免发生意外的行为。
7. 在使用自定义指令时，确保对其参数、值和修饰符的处理正确。在钩子函数中，可以通过`binding`对象获取这些信息。

### 自己实现一个简单v-model

```
directives: {
    "my-model": {
        bind(el, bindding,vnode) {
            el.addEventListener('input', function(event){
                vnode.context[bindding.expression] = event.target.value
            });
            // 这里面的this是Window,而不是vm
            
        }
    }
}
```

我们给输入框的输入绑定了事件,只要输入了数据,就通过VNode拿到vm修改对应的数据

## 生命周期

ue的生命周期是指Vue实例或组件在其整个生命周期内经历的各个阶段。在这些阶段中，**Vue会触发一系列生命周期钩子函数**，这些函数可以让你在特定时机执行自定义的逻辑。了解生命周期及其钩子函数可以帮助你更好地管理组件的状态和资源。

Vue的生命周期主要包括以下几个阶段：

1. 创建阶段（Creation）：在这个阶段，Vue实例或组件开始创建，初始化数据和事件监听器。

   生命周期钩子函数：

   - `beforeCreate`: **在实例初始化之后、数据观测（data observer）和事件配置之前被调用**。
   - `created`: 在实例创建完成后被立即调用。此时，数据观测已经设置，**但DOM还没有生成**，`$el`属性还不可用。

2. 挂载阶段（Mounting）：在这个阶段，Vue实例或组件的模板将被**编译成虚拟DOM并挂载到真实DOM上**。

   生命周期钩子函数：

   - `beforeMount`: 在挂载开始之前被调用。**此时，模板已编译成渲染函数，但还没有挂载到真实DOM上**。
   - `mounted`: **在实例被挂载到真实DOM上后调用**。此时，你可以访问到DOM元素，但需要注意的是，**不保证子组件也都一起被挂载**。

3. 更新阶段（Updating）：在这个阶段，Vue实例或组件的数据发生变化，导致虚拟DOM重新渲染并更新真实DOM。

   生命周期钩子函数：

   - `beforeUpdate`: 在数据变化导致的虚拟DOM重新渲染和打补丁之前被调用。此时，**你可以在这个钩子函数中进一步改变数据，避免不必要的更新**。
   - `updated`: 在数据变化导致的虚拟DOM重新渲染和打补丁之后被调用。此时，**组件DOM已经更新**，**但不保证子组件也都已经更新**。**此时不要改数据**

4. 销毁阶段（Destruction）：在这个阶段，Vue实例或组件将被销毁，**移除所有的事件监听器和子组件**。

   生命周期钩子函数：

   - `beforeDestroy`: 在实例销毁之前被调用。此时，实例仍然完全可用，**你可以在这个钩子函数中执行清理操作**，如取消定时器或事件监听器。
   - `destroyed`: 在实例销毁之后被调用。此时，所有的事件监听器和子组件都已经被移除，**Vue实例的所有属性和方法都不再可用**。

通过在这些生命周期钩子函数中添加自定义逻辑，你可以在特定时机处理特定的任务，例如获取数据、操作DOM元素、监听或取消事件等

> 一定要使用普通方法而不是lambda方法,不然this就是window了

![生命周期](../../img/vue学习assets/生命周期.png)



## 组件

Vue 组件（Component）是一种可复用的、独立的代码单元，它封装了 HTML、CSS 和 JavaScript 代码。组件的目的是将应用的各个部分划分成小的、独立的、可维护的单元，从而提高代码的复用性和可维护性。

组件有以下作用：

1. **模块化**：组件可以将复杂的 UI 划分成小的、独立的模块，使代码结构更加清晰，便于理解和维护。
2. **复用性**：组件可以在多个地方重复使用，避免重复编写相同的代码，提高开发效率。
3. **封装**：组件可以将其内部的实现细节隐藏起来，只暴露必要的接口，降低组件之间的耦合度，使组件更容易替换和升级。

### 非单文件组件

在 Vue 中，你可以使用以下几种方法来注册非单文件组件

**全局注册**：通过 `Vue.component()` 方法注册的组件可以在应用中的任何地方使用。这种方法将组件注册为全局可用。

```
Vue.component('my-component', {
  template: '<div>这是一个全局注册的组件！</div>',
  // 其他组件选项（如 data、methods 等）可在此定义
});

new Vue({
  el: '#app',
});
```

在模板中使用全局注册的组件：

```
<div id="app">
  <my-component></my-component>
</div>
```

**局部注册**：局部注册的组件只能在注册它的 Vue 实例和其子组件中使用。这种方法将组件注册为局部可用。

首先，定义一个组件：

```
const MyComponent = {
  template: '<div>这是一个局部注册的组件！</div>',
  // 其他组件选项（如 data、methods 等）可在此定义
};
```

接下来，在 Vue 实例中局部注册这个组件：

```
new Vue({
  el: '#app',
  components: {
    'my-component': MyComponent,
  },
});
```

在模板中使用局部注册的组件：

```
<div id="app">
  <my-component></my-component>
</div>
```

**使用 `Vue.extend()`**：`Vue.extend()` 函数可以创建一个组件构造器，然后你可以根据需要在不同的地方使用这个构造器来创建组件实例。

首先，使用 `Vue.extend()` 创建一个组件构造器：

```
const MyComponent = Vue.extend({
  template: '<div>这是使用 Vue.extend() 创建的组件！</div>',
  // 其他组件选项（如 data、methods 等）可在此定义
});
```

接下来，在 Vue 实例中使用这个组件构造器：

```
new Vue({
  el: '#app',
  components: {
    'my-component': MyComponent,
  },
});
```

在模板中使用通过 `Vue.extend()` 创建的组件：

```
<div id="app">
  <my-component></my-component>
</div>
```

这些方法都可以用来注册非单文件组件。全局注册的组件可以在整个应用范围内使用，而局部注册的组件仅在特定的 Vue 实例和其子组件中可用。**`Vue.extend()` 方法创建的组件构造器可以在多个地方重复使用**。根据实际需求选择合适的注册方式。

`Vue.extend()` 方法和直接使用字符串注册组件的区别在**于注册到全局组件的时候**, Vue.extend()得到的是一个构造函数,每次都是新的组件,而字符串的格式就相当于一个组件,每次使用都是一个组件,会共享状态

## vue脚手架

Vue 脚手架（Vue CLI，全称 Vue Command Line Interface）是一个基于 Vue.js 的官方命令行工具，旨在帮助开发者快速创建、开发和构建 Vue 项目。Vue 脚手架提供了一套完整的工具和预设选项，让你能专注于编写应用程序代码，而无需关注底层的构建配置和优化过程。

Vue 脚手架的主要功能和用途包括：

1. **快速创建 Vue 项目**：Vue 脚手架提供了一个简单的命令行界面，使得创建新的 Vue 项目变得非常容易。只需几个简单的命令，你就可以创建一个具有预先配置的 Vue 项目，包括目录结构、开发工具配置和基本的 Vue 模板。
2. **项目预设**：Vue 脚手架提供了一些预设选项，允许你根据项目需求选择不同的配置。例如，你可以选择是否需要 Vue Router、Vuex 或者其他第三方库。这可以减轻配置项目的负担，同时确保项目结构的一致性。
3. **开发服务器**：Vue CLI 集成了一个开发服务器（基于 webpack-dev-server），支持热模块替换（HMR）和其他开发功能，使得开发过程更为流畅。
4. **构建和优化**：Vue CLI 提供了一套用于构建和优化 Vue 项目的工具，包括压缩、代码分割、按需加载等功能。这些工具可以帮助你生成高性能的生产环境代码。
5. **可扩展性和插件系统**：Vue CLI 具有强大的可扩展性，允许你根据项目需求自定义构建配置。此外，Vue CLI 还提供了一个插件系统，使得开发者可以方便地为项目添加额外的功能。

总之，Vue 脚手架是一个强大且易于使用的工具，旨在帮助开发者快速创建、开发和构建 Vue 项目。它提供了一套预先配置的工具和选项，使得开发者可以专注于编写应用程序代码，而无需关注底层的构建和优化过程。

> 其实我们所见的功能就是将.vue文件变成html css js这些那

### 如何使用

安装vue/cli

```
npm install -g @vue/cli
```

创建项目

```
vue create projectname
```

启动项目

```
npm run serve
```



写好代码后,构建项目

```
npm run build
```

这将构建并优化项目代码，生成的文件将存放在 `dist` 目录下。



### 项目结构介绍

使用 Vue 脚手架（Vue CLI）创建的项目具有以下目录结构。请注意，根据你在创建项目时选择的预设选项，某些目录和文件可能略有不同。

```
my-project
├── node_modules/         # 项目依赖模块存放目录
├── public/               # 公共资源文件夹，不会被 webpack 处理，会直接复制到构建后的输出目录
│   ├── favicon.ico       # 网站图标
│   └── index.html        # 应用的入口 HTML 文件，可在此文件中添加全局资源引用
├── src/                  # 项目源代码目录
│   ├── assets/           # 资源目录，存放如图片、样式等静态资源，会被 webpack 处理
│   ├── components/       # Vue 组件目录
│   ├── views/            # 页面组件目录，通常用于存放路由组件（当使用 Vue Router 时）
│   ├── App.vue           # 根组件
│   ├── main.js           # 项目的入口文件，包括 Vue 实例化、引入全局资源等
│   └── router.js         # 路由配置文件（当使用 Vue Router 时）
├── tests/                # 测试文件目录
├── .browserslistrc       # 浏览器兼容性配置，用于配置目标浏览器版本
├── .eslintrc.js          # ESLint 配置文件，用于配置代码风格检查规则
├── .gitignore            # Git 忽略文件配置
├── babel.config.js       # Babel 配置文件，用于配置 JavaScript 编译选项
├── package.json          # 项目描述文件，包括项目信息、依赖管理、脚本等
└── vue.config.js         # Vue CLI 配置文件，用于自定义项目的构建配置（如果需要的话）

```



### 做些配置

#### 关闭代码检查

在vue.config.js中这么配置

```
module.exports = {
  lintOnSave: false,
};
```



### 项目分析

我们来看一下main.js这个入口文件

```
import Vue from 'vue'
import App from './App.vue'

// 关闭生产提示
Vue.config.productionTip = false

new Vue({
  // 渲染页面
  render: h => h(App),
}).$mount('#app')   //挂在到id为app的容器中
```

这里使用了一个新的渲染函数,因为我们现在是.vue的格式文件了,而且这里引入的vue是一个残缺版的vue

在开发过程中，**Vue 单文件组件（`.vue` 文件）的模板会被 Vue Loader 预编译为渲染函数**。因此，运行时版本的 Vue（不包含模板编译器）已经可以正常工作。这意味着，项目中的模板在构建时就已经被编译成 JavaScript，**不需要在浏览器中再进行模板编译**。这有助于提高性能和减小输出文件的体积。



## 其他内容

### ref属性

在 Vue 中，`ref` 是一个特殊的属性，用于获取对 DOM 元素或 Vue 组件实例的引用。`ref` 属性的主要作用是允许你在 Vue 实例的方法或计算属性中访问 **DOM 元素**或**子组件实例(VC0**，从而可以对它们进行操作或获取信息。

使用 `ref` 属性的步骤如下：

1. 在需要引用的 DOM 元素或组件上添加 `ref` 属性，并为其分配一个唯一的标识符（字符串）。

   ```
   <input ref="myInput" />
   <my-component ref="myComponent"></my-component>
   ```

2. 在 Vue 实例中通过 `this.$refs` 对象访问指定的 `ref`。

   ```
   export default {
     methods: {
       doSomething() {
         // 访问 DOM 元素
         const myInputElement = this.$refs.myInput;
         console.log(myInputElement.value);
   
         // 访问组件实例
         const myComponentInstance = this.$refs.myComponent;
         myComponentInstance.someMethod();
       },
     },
   };
   ```

需要注意的是，`ref` 属性不是响应式的，因此在引用发生变化时不会触发 Vue 实例的更新。另外，`ref` 属性仅在 Vue 实例渲染完成后可用。在实例创建期间（如 `created` 生命周期钩子中）访问 `this.$refs` 可能会得到 `undefined`。因此，在需要使用 `ref` 的场景中，通常会在 `mounted` 或 `updated` 生命周期钩子中进行操作。

总之，`ref` 属性使你能够在 Vue 实例中访问和操作 DOM 元素或子组件实例，从而实现更复杂的交互和功能。

### props属性

`props` 是 Vue 组件中的一个概念，表示属性。它允许父组件向子组件传递数据。`props` 的主要用途是实现组件之间的数据流动和通信，使组件更加灵活和可复用。组件可以根据接收到的 `props` 数据来调整其行为和显示内容，这样组件就可以在不同的场景下重复使用。

关于 `props`，有一些注意事项：

1. **单向数据流**：`props` 数据流动是单向的，从父组件流向子组件。为了保持数据的一致性和可预测性，不建议子组件直接修改 `props`。如果需要在子组件中改变 `props` 的值，可以创建一个局部变量或使用计算属性。
2. **类型检查**：为了避免潜在的错误和数据不一致，建议在子组件中为 `props` 定义类型。Vue 提供了一个 `PropType` 工具，用于定义 `props` 的类型。这样，在传递非预期类型的数据时，Vue 将发出警告。
3. **默认值**：为了让组件在未接收到特定 `props` 数据时仍能正常工作，可以为 `props` 提供默认值。在定义 `props` 时，可以使用 `default` 选项来设置默认值。
4. **必需属性**：在某些场景下，子组件可能需要父组件传递某个 `props` 才能正常工作。为了确保组件的正确使用，可以将这些 `props` 标记为必需。在定义 `props` 时，可以使用 `required` 选项设置为 `true`。
5. **避免修改复杂数据类型**：虽然不建议直接修改 `props`，但在处理复杂数据类型（如对象和数组）时，Vue 无法阻止你修改 `props`。修改复杂数据类型可能导致父组件和子组件的数据不一致。为了避免这种情况，可以使用计算属性或方法创建数据副本，然后在子组件中操作副本。

props的数据是优先被代理到vc上面去的,  在beforecreate之前就有了,因此我们可以在data属性中使用

# 总结

## 计算属性与监视属性对比

计算属性和监视属性都是 Vue 中用于处理属性值变化的方法，但它们各自适用于不同的场景。以下是计算属性和监视属性的对比，以及它们的优缺点：

计算属性（Computed properties）：

优点：

1. 缓存：计算属性的结果会被缓存，只有当依赖的属性发生变化时，计算属性才会重新计算。这有助于提高性能，特别是在计算过程复杂或计算代价较高的情况下。
2. 响应式：计算属性自动跟踪它们所依赖的属性。当依赖的属性发生变化时，计算属性会自动更新。这使得计算属性在处理复杂逻辑和依赖关系时非常方便。
3. 可读性：计算属性可以将复杂的逻辑封装在一个属性中，提高代码的可读性和可维护性。

缺点：

1. 无法处理异步操作：计算属性的计算函数必须是同步的，无法直接处理异步操作，如 AJAX 请求等。

监视属性（Watch properties）：

优点：

1. 异步操作：监视属性在属性值发生变化时执行回调函数，可以很容易地处理异步操作，如 AJAX 请求等。
2. 灵活性：监视属性允许你针对属性值的变化执行特定操作，可以处理一些特定的副作用。

缺点：

1. 无缓存：监视属性的回调函数每次都会执行，不具备计算属性的缓存特性。因此，在性能方面可能不如计算属性。
2. 可读性：相较于计算属性，监视属性的逻辑可能分散在多个地方，导致代码可读性和可维护性较差。

总结： 计算属性和监视属性各有优缺点，它们适用于不同的场景。在需要根据其他属性计算一个值的情况下，计算属性通常是更好的选择。而在处理异步操作或需要根据属性值变化执行特定操作的场景中，监视属性可能更适合。根据实际需求和场景选择适当的方法来实现功能。