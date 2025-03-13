class Node {
public:
    int val;
    vector<Node*> prerequisites;
    Node() {
        val = 0;
        prerequisites = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        prerequisites = vector<Node*>();
    }
    Node(int _val, vector<Node*> _prerequisites) {
        val = _val;
        prerequisites = _prerequisites;
    }
};

class Solution {
public:
    bool hasCycle(Node* node, vector<bool>& visited, vector<bool>& inStack) {
        int courseId = node->val;
        visited[courseId] = true;
        inStack[courseId] = true;
        for (Node* prereq : node->prerequisites) {
            int prereqId = prereq->val;
            if (!visited[prereqId]) {
                if (hasCycle(prereq, visited, inStack)) return true;
            }
            else if (inStack[prereqId]) return true;
        }
        inStack[courseId] = false;
        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, Node*> courses;
        for(vector<int> relation : prerequisites) {
            int course = relation[0];
            int prerequisite = relation[1];
            if (courses.find(course) == courses.end()) courses[course] = new Node(course);
            if (courses.find(prerequisite) == courses.end()) courses[prerequisite] = new Node(prerequisite);
            courses[course]->prerequisites.push_back(courses[prerequisite]);
        }
        vector<bool> visited(numCourses, false);
        vector<bool> inStack(numCourses, false);
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i] && courses.find(i) != courses.end() && hasCycle(courses[i], visited, inStack)) return false;
        }
        return true;
    }
};