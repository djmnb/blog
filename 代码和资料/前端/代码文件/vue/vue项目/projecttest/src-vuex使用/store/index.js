
import vuex from "vuex"
import vue from "vue"

const student = {
    state: {
        studentlist:["djm"]
    },
    namespaced:true
}

const teacher = {
    state: {
        teacherlist:["djm"]
    },
    namespaced:true
}

vue.use(vuex)
export default new vuex.Store({
    modules: {
        student,teacher
    }
})


