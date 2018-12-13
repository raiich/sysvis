example_statement = """
group clients {
  c1;
  c2;
};

group kvs {
  node [shape='cylinder'];
  s1;
  s2;
  s3;
  hinted_hand_off[shape='box'];
};
---
c1 -> s1 [label='write x=1\\n...', 'stroke-dasharray'='4'];
c1 -> s2 [label='write x=1'];
s1[label='x=1'];
s2[label='x=1'];
---
c2[label='x=1'];
c2 -> s2 [label='read x=1'];
"""

example_statement = """
group c1 {
  me[shape='person'];
  client1;
};
group service1 {
  zone az1 {
    proxy1;
    backend1
  };
  zone az2 {
    proxy2;
    backend2
  };
}

---
me -> client1;
client1 -> proxy1;
client1 -> proxy2;
proxy1 -> backend1;
proxy2 -> backend2;
"""