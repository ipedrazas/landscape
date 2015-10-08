# Landscape

Landscape allows you to create a map of your applications.

```
                 +----------+    +----------+                      
                 | Person   |    | Person   |                      
                 +---------++    +--+-------+                      
                           |        |                              
                           |        |                              
                           |        |                              
                       +---v--------v-+                            
                       |              |                            
                  +---->  Application <--------------------+       
                  |    |              |                    |       
                  |    +-----^--------+                    |       
                  |          |                             |       
                  |          |                             |       
                  |          |                             |       
                  |          |                             |       
         +--------+-----+    |  +------------+      +------+------+
         |  Component   |    |  | Component  |      |  Component  |
         |              |    +--+            |      |             |
         +-------^------+       +------------+      +-------------+
                 |                                                 
                 |                                                 
                 |                                                 
                 |                                                 
+------------+   |   +-----------+                                 
| Component  +---+---+ Component |                                 
|            |       |           |                                 
+------------+       +-----------+    
```

The system allows you to define and link components vi a UI or an API
